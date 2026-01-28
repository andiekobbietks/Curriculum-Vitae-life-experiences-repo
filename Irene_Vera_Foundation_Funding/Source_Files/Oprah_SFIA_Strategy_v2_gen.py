
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.units import cm

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            rightMargin=2.5*cm, leftMargin=2.5*cm,
                            topMargin=2.5*cm, bottomMargin=2.5*cm)
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom Colors
    PRIMARY_COLOR = colors.HexColor("#5D4037")
    SECONDARY_COLOR = colors.HexColor("#A0522D")
    
    # Custom Styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=24,
        textColor=PRIMARY_COLOR,
        spaceAfter=20,
        alignment=1 # Center
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Title'],
        fontName='Helvetica-Bold',
        fontSize=18,
        textColor=SECONDARY_COLOR,
        spaceAfter=40,
        alignment=1
    )
    
    h1_style = ParagraphStyle(
        'CustomH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=16,
        textColor=PRIMARY_COLOR,
        spaceBefore=20,
        spaceAfter=10,
        borderPadding=5,
        borderColor=PRIMARY_COLOR,
        borderWidth=0,
        borderBottomWidth=1
    )
    
    h2_style = ParagraphStyle(
        'CustomH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=14,
        textColor=SECONDARY_COLOR,
        spaceBefore=15,
        spaceAfter=8
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11,
        leading=14,
        spaceAfter=10
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=normal_style,
        leftIndent=20,
        firstLineIndent=0,
        spaceAfter=5
    )

    # --- Title Page ---
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("Strategy & Capability Framework v2", title_style))
    story.append(Paragraph("Transfer of Knowledge: From FirstGens UK to New Ventures", subtitle_style))
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("<b>Prepared For:</b><br/>Executive Board & Strategic Partners", normal_style))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("<b>Focus Areas:</b><br/>SFIA Skills Alignment<br/>Resource Mobilisation (Fund Directory)<br/>Institutional Orchestration", normal_style))
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("<b>Date:</b> January 2026", normal_style))
    story.append(PageBreak())

    # --- Section 1: Executive Narrative ---
    story.append(Paragraph("EXECUTIVE NARRATIVE: THE TRANSFER OF KNOWLEDGE", h1_style))
    
    text = """This strategy document explicitly outlines the transition from a startup mentality to an institutional architecture phase. We are not operating as a tentative new entity; rather, we are applying the <b>"FirstGens UK Pattern"</b>—a proven, funded methodology architected by Andie (Technical Steward) over a 70-month tenure."""
    story.append(Paragraph(text, normal_style))
    
    story.append(Paragraph("Proven Methodology, Not Experimentation", h2_style))
    text = """The core proposition is a direct transfer of high-value intellectual property and operational patterns. Andie is not merely a technical resource but the architect of a system that has already delivered significant capital and reputational value."""
    story.append(Paragraph(text, normal_style))
    
    bullets = [
        ListItem(Paragraph("<b>Secured Funding:</b> £46,000 in direct grants and awards (FEA, GirlDreamer, Digitization).", bullet_style)),
        ListItem(Paragraph("<b>Cost Avoidance:</b> £15,000 in technical debt and operational risk mitigation through 'Vetted Roadmaps' and technical scaffolding.", bullet_style)),
        ListItem(Paragraph("<b>Institutional Logic:</b> We are applying the same 'V-shaped' strategic framework that transformed a student blog into a Diana Award-winning national institution.", bullet_style))
    ]
    story.append(ListFlowable(bullets, bulletType='bullet', start='circle'))

    # --- Section 2: SFIA Responsibility Mapping ---
    story.append(Paragraph("SFIA RESPONSIBILITY MAPPING", h1_style))
    story.append(Paragraph("To professionalize our operations and align with industry standards, key roles are mapped to the <b>Skills Framework for the Information Age (SFIA)</b>.", normal_style))

    story.append(Paragraph("Andie: Technical Steward", h2_style))
    story.append(Paragraph("<b>Role Alignment: Strategy & Architecture (Level 5)</b>", normal_style))
    story.append(Paragraph("Andie operates at the intersection of technical execution and strategic direction, ensuring that technology investments deliver measurable business value.", normal_style))
    
    bullets_andie = [
        ListItem(Paragraph("<b>Ensure & Advise:</b> Provides authority on technical frameworks and digital roadmap viability.", bullet_style)),
        ListItem(Paragraph("<b>Strategic Scoping:</b> Demonstrated by the 'Decolonial Genesis' pattern—aligning technical stacks with sociological theory (e.g., BSWN 'UnMuseum' bid).", bullet_style)),
        ListItem(Paragraph("<b>Service Stewardship:</b> Responsible for the 'Point' of the V-shape—high-availability troubleshooting and resilience (e.g., NavigateU PWA, Wazuh security hardening).", bullet_style))
    ]
    story.append(ListFlowable(bullets_andie, bulletType='bullet', start='circle'))

    story.append(Paragraph("Oprah: Strategic Lead", h2_style))
    story.append(Paragraph("<b>Role Alignment: Relationship Management (Level 6)</b>", normal_style))
    story.append(Paragraph("Oprah operates at the initiation and influence level, orchestrating the ecosystem relationships that drive funding and policy change.", normal_style))
    
    bullets_oprah = [
        ListItem(Paragraph("<b>Initiate & Influence:</b> Owners of high-level stakeholder relationships (InnovateUK, Microsoft, Government bodies).", bullet_style)),
        ListItem(Paragraph("<b>Strategic Orchestration:</b> Convening complex ecosystems to generate institutional value.", bullet_style)),
        ListItem(Paragraph("<b>Resource Mobilisation:</b> Transforming relational capital into liquid assets and strategic partnerships.", bullet_style))
    ]
    story.append(ListFlowable(bullets_oprah, bulletType='bullet', start='circle'))
    
    story.append(PageBreak())

    # --- Section 3: Expanded Fund Directory ---
    story.append(Paragraph("EXPANDED FUND DIRECTORY", h1_style))
    story.append(Paragraph("This directory categorizes funding sources identified through the 'FirstGens UK Pattern' and recent strategic scoping. These are not merely potential sources but targeted partners where our narrative has proven resonance.", normal_style))

    # Tier 1
    story.append(Paragraph("Tier 1: Keystone Funding (Core Strategic Pillars)", h2_style))
    story.append(Paragraph("<i>Large-scale, multi-year support for core operations and R&D.</i>", normal_style))
    
    story.append(Paragraph("<b>Innovate UK (Smart Grants / Young Innovators)</b>", normal_style))
    story.append(Paragraph("<b>Focus:</b> Disrupted, high-growth innovation and R&D.", normal_style))
    story.append(Paragraph("<b>Fit:</b> The 'Young Innovator Award' (£25k) establishes a precedent. Our focus on digital transformation and 'Tech for Good' platforms (like NavigateU) aligns perfectly with their objective to scale impact-driven innovations.", normal_style))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>BSWN (Black South West Network) 'UnMuseum'</b>", normal_style))
    story.append(Paragraph("<b>Focus:</b> Cultural heritage, decolonisation, and digital archiving.", normal_style))
    story.append(Paragraph("<b>Fit:</b> A primary target for the 'Left Arm' of our strategy (Decolonial Theory). The £18.5k digitization work positions us as ideal partners for the 'UnMuseum' bid, providing the technical infrastructure to preserve and present Black cultural heritage.", normal_style))

    # Tier 2
    story.append(Paragraph("Tier 2: Enablers (Specific Project Support)", h2_style))
    story.append(Paragraph("<i>Targeted grants for specific demographics or operational phases.</i>", normal_style))

    story.append(Paragraph("<b>Fair Education Alliance (FEA) Innovation Award</b>", normal_style))
    story.append(Paragraph("<b>Focus:</b> Educational equity and social mobility.", normal_style))
    story.append(Paragraph("<b>Fit:</b> Having secured £25,000 previously, this fund validates our data-driven approach to social impact (addressing the 13% deprivation gap). It provides not just capital but the 'Insider' status required for larger institutional bids.", normal_style))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>GirlDreamer / Mettle 'Dream Fund'</b>", normal_style))
    story.append(Paragraph("<b>Focus:</b> Early-stage support for women of colour-led organizations.", normal_style))
    story.append(Paragraph("<b>Fit:</b> A proven source (£2,500 secured). This fund acts as a rapid-response enabler for 'Right Arm' ecosystem activities, financing early-stage pilots or community engagement events without the heavy administrative burden of government grants.", normal_style))

    # Tier 3
    story.append(Paragraph("Tier 3: Partners (Ecosystem & Relational Capital)", h2_style))
    story.append(Paragraph("<i>Strategic alignment for non-financial or indirect support.</i>", normal_style))

    story.append(Paragraph("<b>Prince's Trust</b>", normal_style))
    story.append(Paragraph("<b>Focus:</b> Enterprise launch and youth employment.", normal_style))
    story.append(Paragraph("<b>Fit:</b> An early-stage ecosystem partner. While direct funding is smaller, their brand endorsement serves as a trust signal to larger Tier 1 funders.", normal_style))
    story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("<b>Microsoft / Corporate Digitization Grants</b>", normal_style))
    story.append(Paragraph("<b>Focus:</b> Digital inclusion and non-profit tech acceleration.", normal_style))
    story.append(Paragraph("<b>Fit:</b> Leveraged through our 'Service Desk' DNA. These partners provide the software infrastructure (Azure, Teams, M365) that constitutes our £15k cost avoidance strategy.", normal_style))

    # --- Conclusion ---
    story.append(Paragraph("CONCLUSION", h1_style))
    story.append(Paragraph("This v2 strategy document confirms that we are entering the next phase with a significant competitive advantage. By formalizing the SFIA Level 5/6 partnership between Andie and Oprah and activating the Tier 1-3 funding directory, we are operationalizing a legacy of success.", normal_style))

    doc.build(story)
    print(f"PDF generated successfully: {filename}")

if __name__ == "__main__":
    create_pdf("Oprah_SFIA_Strategy_v2.pdf")
