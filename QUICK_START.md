# Quick Start Guide

This guide will help you start documenting your first organization in under 10 minutes.

## Prerequisites

- Clone this repository
- Basic knowledge of Markdown
- A text editor

## Step-by-Step: Document Your First Organization

### Step 1: Create the Folder Structure (1 minute)

Replace `[your-company-name]` with the actual organization name (use lowercase with hyphens):

```bash
# Navigate to the repository
cd life-experiences-repo

# Create the organization structure
ORG_NAME="your-company-name"  # e.g., "acme-corporation"
mkdir -p "organizations/${ORG_NAME}/projects"
mkdir -p "organizations/${ORG_NAME}/evidence"
mkdir -p "organizations/${ORG_NAME}/assets/images"
mkdir -p "organizations/${ORG_NAME}/assets/documents"
mkdir -p "organizations/${ORG_NAME}/assets/certificates"
```

### Step 2: Copy the Organization Template (30 seconds)

```bash
cp templates/ORGANIZATION_README_TEMPLATE.md "organizations/${ORG_NAME}/README.md"
```

### Step 3: Fill in Basic Information (5 minutes)

Open `organizations/[your-company-name]/README.md` and fill in:

1. **Overview section** (top of file):
   - Replace `[Organization Name]` with the actual company name
   - Fill in `[Start Date]` and `[End Date or Present]`
   - Add your role(s)
   - Add location
   - Add organization type (Startup, Enterprise, etc.)
   - Add brief description

2. **Timeline**:
   - Update the Gantt chart with your actual dates and roles
   ```mermaid
   gantt
       title My Journey at [Organization Name]
       dateFormat  YYYY-MM-DD
       section Roles
       Software Engineer      :2020-01-01, 365d
       Senior Engineer        :2021-01-01, 365d
   ```

3. **Key Milestones**:
   - Add 3-5 important dates and what happened

### Step 4: Add One Contribution (3 minutes)

In the "Responsibilities & Contributions" section, add at least one project or contribution:

```markdown
### Technical Contributions

- **[Project Name]**
  - Description: [What you built/did]
  - Technologies: [List technologies used]
  - Impact: [What was the outcome]
  - Evidence: [Will add later]
```

### Step 5: Save and Preview

1. Save the file
2. View it in GitHub or a Markdown preview tool
3. Check that Mermaid charts render correctly

## Next Steps

After your first organization is documented, you can:

### Add a Project (Optional)

```bash
cp templates/PROJECT_TEMPLATE.md "organizations/${ORG_NAME}/projects/my-first-project.md"
```

Then fill in the project template with details about a significant project.

### Add Evidence (Optional)

```bash
cp templates/EVIDENCE_TEMPLATE.md "organizations/${ORG_NAME}/evidence/code-my-contribution.md"
```

Add a code sample, design document, or other evidence of your work.

### Update the Organizations README

Edit `organizations/README.md` and add your organization to the list:

```markdown
### Current Organizations

- **[Your Company](your-company-name/README.md)** *(Start - End)*
  - Role: Your Role
  - Focus: Brief description
  - Key Achievement: One major achievement
```

## Tips for Success

### Start Small
- Don't try to document everything at once
- Start with one organization, one project, one piece of evidence
- Add more detail over time

### Be Consistent
- Use the same format for all organizations
- Follow the template structure
- Use similar level of detail across sections

### Focus on Impact
- Always include "why it mattered"
- Use numbers and metrics when possible
- Connect technical work to business outcomes

### Update Regularly
- Set aside time monthly or quarterly
- Add new projects as they complete
- Refine descriptions as you gain perspective

## Common Issues

### Mermaid Charts Not Rendering?

Ensure your Markdown viewer supports Mermaid. GitHub does automatically. For local viewing, use:
- VS Code with "Markdown Preview Mermaid Support" extension
- [Mermaid Live Editor](https://mermaid.live/) for testing

### Too Much Detail?

Use collapsible sections for detailed content:

```markdown
<details>
<summary>View detailed code</summary>

Your detailed content here...

</details>
```

### Can't Remember Details?

It's OK to start with what you remember:
- Fill in placeholders with estimates
- Mark sections as "[TODO]" to revisit
- Add detail as you remember or find it

## Example Timeline

Here's a realistic timeline for documenting your professional history:

- **Week 1**: Document current organization (overview + 1-2 key projects)
- **Week 2**: Add evidence for current organization (2-3 pieces)
- **Week 3**: Document most recent past organization
- **Week 4**: Add older organizations (can be less detailed)
- **Ongoing**: Add new projects and evidence as they happen

## Need Help?

- Review the [Templates Guide](templates/README.md) for detailed instructions
- Look at the [Example Tech Company](organizations/example-tech-company/README.md) for reference
- Check individual templates for field-by-field guidance

---

**Remember**: Perfect is the enemy of done. Start with something, even if it's incomplete, and refine over time!
