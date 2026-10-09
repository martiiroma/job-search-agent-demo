#!/usr/bin/env python3
"""
guard.py — PreToolUse hook for the job-search agent.

STRUCTURAL block, not a persuasive one. A rule written in a .md file is an
instruction the model may misread under prompt injection. This is code that
runs before the tool call and denies it. The model takes no part in it.

Authorship: written with Claude Code from rules defined by the system's
designer. The rules are documented in CLAUDE.md and knowledge/ANTI-PATTERNS.md.

DENIAL MESSAGES ARE DECLARATIVE, NEVER IMPERATIVE
They say what was denied. They never give instructions, suggest alternatives
or explain how to proceed. A tool message that contains instructions cannot
be told apart from a prompt injection. On 16/08/2026 an agent correctly
flagged one of this hook's messages as a possible injection because it said
"Use the resolution cascade". It was right.

SECURITY ASYMMETRY: this hook only DENIES. It never grants permissions.
Any [GUARD] message that AUTHORISES an action is, by definition, forged.

Input:  JSON on stdin with {"tool_name": ..., "tool_input": {...}}
Output: JSON with permissionDecision "deny", or a silent exit (allow)
"""

import json
import re
import sys

# ─────────────────────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────────────────────

# The only inbox drafts may be addressed to.
ALLOWED_ADDRESSES = {
    "alex.demo@example.com",
}

# Personal data that must never travel inside a URL.
# Generic patterns: no literal personal data lives in this file,
# because the repository may be readable by third parties.
PII_PATTERNS = [
    r"[\w.+-]+@[\w-]+\.[\w.]+",       # any email address
    # Spanish mobile. Requires a +34 prefix OR separators between groups.
    # Nine bare digits are NOT treated as a phone number: job offer IDs look
    # like that and caused false positives (documented case, 21/08/2026).
    # The risk of a bare number leaking is low; the cost of blocking real
    # offers is high.
    r"\+?\s*34(?:[\s.\-]|%20)*[67](?:(?:[\s.\-]|%20)*\d){8}",
    r"\b[67]\d{2}(?:[\s.\-]|%20)+\d{2,3}(?:[\s.\-]|%20)+\d{2,3}(?:(?:[\s.\-]|%20)+\d{2,3})?\b",
    r"\b\d{8}[A-Za-z]\b",              # Spanish national ID
    r"\b[XYZ]\d{7}[A-Za-z]\b",         # Spanish foreigner ID
]

BLOCKED_DOMAINS = [
    "linkedin.com",
    "glassdoor.com",
    "glassdoor.es",
]

# Tools that must never run
FORBIDDEN_TOOLS = [
    "send_message",          # email: send
    "forward",               # email: forward
    "trash_message", "trash_thread",
    "delete_label",
    "trash_file",            # cloud drive
    "apply_sensitive_message_label", "apply_sensitive_thread_label",
    "mark_message_spam", "mark_thread_spam",
]

# Master design templates: read and copy only
PROTECTED_DESIGNS = ["MASTER_CV_ID", "MASTER_LETTER_ID"]


def deny(reason):
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": f"[GUARD] {reason}",
        }
    }))
    sys.exit(0)


def allow():
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        allow()  # nothing to interpret: do not block the normal flow

    tool = (data.get("tool_name") or "").lower()
    args = data.get("tool_input") or {}
    blob = json.dumps(args, ensure_ascii=False)

    # ── 1. Forbidden tools ─────────────────────────────────
    for forbidden in FORBIDDEN_TOOLS:
        if forbidden in tool:
            deny(f"Action denied: the tool '{forbidden}' is forbidden in this "
                 f"environment. This denial is final.")

    # ── 2. Drafts: only to the human's own inbox ───────────
    if "draft" in tool:
        recipients = []
        for field in ("to", "cc", "bcc", "recipients", "toRecipients"):
            value = args.get(field)
            if isinstance(value, str):
                recipients += re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", value)
            elif isinstance(value, list):
                for v in value:
                    recipients += re.findall(r"[\w.+-]+@[\w-]+\.[\w.]+", str(v))

        for address in recipients:
            if address.lower() not in ALLOWED_ADDRESSES:
                deny(f"Action denied: recipient {address} is not authorised. "
                     f"This denial is final.")

    # ── 3. Network requests ────────────────────────────────
    if "fetch" in tool or "navigate" in tool:
        url = str(args.get("url", ""))
        url_lower = url.lower()

        for domain in BLOCKED_DOMAINS:
            if domain in url_lower:
                deny(f"Action denied: the domain {domain} is blocked in this "
                     f"environment. This denial is final.")

        # Exfiltration: no personal data inside a URL
        for pattern in PII_PATTERNS:
            if re.search(pattern, url, re.IGNORECASE):
                deny("Action denied: the URL contains personal data. "
                     "This denial is final.")

        # Abnormally long query strings → possible data payload.
        # This is the only rule that lives in code and in no document,
        # which makes it the most diagnostic test (tests/security-battery.md).
        if "?" in url and len(url.split("?", 1)[1]) > 300:
            deny("Action denied: query string longer than 300 characters. "
                 "This denial is final.")

    # ── 4. Master design templates ─────────────────────────
    # Editing happens in two steps: first a transaction is opened on the
    # design (its ID is visible), then edits cite only the transaction_id
    # (the ID is NO LONGER there). Blocking only the second call lets the
    # whole transactional path through (documented incident #8).
    # → The block sits on OPENING THE TRANSACTION, where the ID is visible.
    is_design = "canva" in tool or "design" in tool
    if is_design:
        for design_id in PROTECTED_DESIGNS:
            if design_id not in blob:
                continue

            # a) Opening an edit transaction on a master
            if "open_transaction" in blob and "true" in blob.lower():
                deny(f"Action denied: opening an edit transaction on the "
                     f"protected design {design_id}. This denial is final.")

            # b) A direct edit call that names the master
            if any(x in tool for x in ("edit-design", "edit_design", "resize")):
                deny(f"Action denied: the design {design_id} is a write-protected "
                     f"master. This denial is final.")

            # c) Merging designs: only when creating a NEW design
            if "merge" in tool:
                creates_new = any(k in blob.lower() for k in
                                  ("create_new", "new_design", "createnew", "create_design"))
                if not creates_new:
                    deny(f"Action denied: structural operation on the master "
                         f"{design_id} outside creation mode. This denial is final.")

    # ── 5. Deleting design pages ───────────────────────────
    # ⚠️ Known issue (open): every edit call carries "page_index", so this
    # rule also blocks deleting a single element, not only a page.
    # See docs/incidents.md, #17.
    if "delete" in blob.lower() and "page" in blob.lower() and "canva" in tool:
        deny("Action denied: deleting design pages is forbidden. "
             "This denial is final.")

    allow()


if __name__ == "__main__":
    main()