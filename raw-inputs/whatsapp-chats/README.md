# WhatsApp Chats Intake

This folder is your **landing zone** for WhatsApp chat exports about your work. Dump your chat exports here, and GitHub Copilot will help crawl, analyze, and document them into the proper folders with all the evidence, history, and lessons learned.

## Quick Start

1. **Export your WhatsApp chat** (see instructions below)
2. **Drop the exported file** into the `unprocessed/` folder
3. **Ask GitHub Copilot** to process it with a prompt like:
   > "Process the WhatsApp chat in `raw-inputs/whatsapp-chats/unprocessed/` and extract:
   > - Key work discussions and decisions
   > - Evidence of projects and contributions
   > - Lessons learned and insights
   > - Timeline of events
   > - Create proper documentation in the organizations folder"

## Folder Structure

```
whatsapp-chats/
├── README.md           # This file - instructions and guides
├── unprocessed/        # 📥 DROP NEW CHAT EXPORTS HERE
├── processed/          # ✅ Chats that have been documented
├── by-project/         # 📁 Chats organized by project name
├── by-date/            # 📅 Chats organized by date/period
└── media/              # 🖼️ Images, documents, voice notes
```

## How to Export WhatsApp Chats

### On iPhone
1. Open the WhatsApp chat you want to export
2. Tap the contact/group name at the top
3. Scroll down and tap **Export Chat**
4. Choose **Attach Media** (to include images/documents) or **Without Media**
5. Share/Save the exported file
6. Transfer to your computer and place in `unprocessed/`

### On Android
1. Open the WhatsApp chat you want to export
2. Tap the three dots (⋮) in the top right
3. Tap **More** → **Export chat**
4. Choose **Include Media** or **Without Media**
5. Save or share the exported file
6. Transfer to your computer and place in `unprocessed/`

## What GitHub Copilot Will Extract

When you ask Copilot to process your chats, it can identify and document:

### 📋 Evidence & History
- Project discussions and decisions
- Problem-solving conversations
- Technical implementations mentioned
- Stakeholder communications
- Timeline of events and milestones

### 🎯 Lessons Learned
- Challenges faced and how they were overcome
- What worked well and what didn't
- Advice and insights shared
- Skills demonstrated or learned

### 📊 Metrics & Impact
- Deadlines mentioned and met
- Results and outcomes discussed
- Feedback received
- Recognition and achievements

### 👥 Context
- Team dynamics and collaborations
- Stakeholder relationships
- Role and responsibilities demonstrated

## Processing Prompts for GitHub Copilot

Use these prompts to help Copilot process your chats effectively:

### Full Analysis
```
Analyze the WhatsApp chat export in `raw-inputs/whatsapp-chats/unprocessed/[filename]`:

1. Summarize the key work-related discussions
2. Extract evidence of projects, contributions, and impact
3. Identify lessons learned and insights
4. Create a timeline of important events
5. Generate documentation following the templates in this repo
6. Suggest which organization/project folder this belongs to
```

### Lessons Learned Focus
```
Review the WhatsApp chat in `raw-inputs/whatsapp-chats/unprocessed/[filename]` and extract:

1. Challenges and obstacles mentioned
2. How problems were solved
3. What went well
4. What could have been done differently
5. Key takeaways and insights

Format as a lessons learned document using the lessons learned template (templates/LESSONS_LEARNED_TEMPLATE.md).
```

### Project Evidence
```
From the WhatsApp chat in `raw-inputs/whatsapp-chats/unprocessed/[filename]`:

1. Identify project-related discussions
2. Extract my specific contributions and actions
3. Note outcomes and results mentioned
4. Format as STAR (Situation, Task, Action, Result) evidence
5. Create evidence file in the appropriate organization folder
```

### Timeline Creation
```
Create a timeline from the WhatsApp chat in `raw-inputs/whatsapp-chats/unprocessed/[filename]`:

1. Extract all dated events and milestones
2. Identify key decision points
3. Map progress of projects/tasks
4. Generate a Mermaid Gantt chart
5. Note any deadlines met or challenges faced
```

## Naming Conventions

When placing files in this folder, use descriptive names:

### Unprocessed Files
```
YYYY-MM-DD_[project-or-topic]_[chat-type].txt

Examples:
2026-01-15_payment-system-project_team-chat.txt
2026-01-20_client-feedback_one-on-one.txt
2025-12_q4-review_manager-chat.txt
```

### Processed Files (after documentation)
```
YYYY-MM-DD_[project-or-topic]_PROCESSED.txt

Examples:
2026-01-15_payment-system-project_team-chat_PROCESSED.txt
```

## Best Practices

### Before Dumping
- ✅ Review chat for any highly sensitive information
- ✅ Note the approximate date range of the chat
- ✅ Identify which project/organization it relates to
- ✅ Export with media if images/documents are relevant

### When Processing
- ✅ Ask Copilot to anonymize sensitive names if needed
- ✅ Review extracted content before adding to main docs
- ✅ Link generated evidence to relevant project files
- ✅ Move processed files to `processed/` folder

### After Processing
- ✅ Verify documentation accuracy
- ✅ Add cross-references to other evidence
- ✅ Update organization/project README if needed
- ✅ Delete raw chat if no longer needed

## Privacy & Security Notes

⚠️ **Important Considerations:**

1. **Personal Information**: Chat exports may contain personal details. Review before committing to a public repository.

2. **Confidential Business Info**: Some work discussions may be confidential. Anonymize or redact as appropriate.

3. **Third-Party Consent**: Be mindful of including others' messages. Consider summarizing instead of quoting directly.

4. **Media Files**: Images and documents in `media/` folder should be reviewed for sensitive content.

5. **Git History**: Once committed, content lives in git history. Be careful what you commit.

## Example Workflow

```
1. You have a WhatsApp group chat about "Project Phoenix"
   
2. Export: "WhatsApp Chat with Project Phoenix Team.txt"

3. Rename: "2026-01-project-phoenix-team-chat.txt"

4. Place in: raw-inputs/whatsapp-chats/unprocessed/

5. Ask Copilot:
   "Process the chat export in unprocessed/2026-01-project-phoenix-team-chat.txt
    Create documentation in organizations/[company]/projects/"

6. Review generated documentation

7. Move to: raw-inputs/whatsapp-chats/processed/
   (with _PROCESSED suffix)

8. Commit the new documentation (not the raw chat if sensitive)
```

---

**Ready to start?** Drop your first chat export in the `unprocessed/` folder! 📱➡️📂
