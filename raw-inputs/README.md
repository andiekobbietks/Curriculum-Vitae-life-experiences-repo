# Raw Inputs

This folder serves as the **intake zone** for raw data that needs to be processed and documented into the appropriate sections of this repository.

## Purpose

When you have raw evidence, chats, notes, or other materials about your work experiences, dump them here first. GitHub Copilot can then help crawl, analyze, and organize this content into properly structured documentation.

## Folder Structure

```
raw-inputs/
├── README.md                 # This file
├── whatsapp-chats/          # WhatsApp chat exports
│   ├── README.md            # Instructions for WhatsApp exports
│   ├── unprocessed/         # New chat exports to be processed
│   ├── processed/           # Chats that have been documented
│   ├── by-project/          # Chats organized by project
│   ├── by-date/             # Chats organized by date
│   └── media/               # Images, documents from chats
└── [future folders]/        # Other input types (emails, notes, etc.)
```

## Workflow

1. **Dump** - Export and place raw files in the appropriate `unprocessed/` folder
2. **Request** - Ask GitHub Copilot to process the content
3. **Review** - Check the generated documentation
4. **Organize** - Move processed files to `processed/` folder
5. **Update** - Link evidence to relevant projects/organizations

## Supported Input Types

- ✅ WhatsApp chat exports (.txt, .zip)
- 🔜 Email exports
- 🔜 Meeting notes
- 🔜 Slack exports
- 🔜 Screenshots and images

---

**Note**: Raw inputs may contain sensitive information. Review generated documentation before committing to ensure no confidential data is exposed.
