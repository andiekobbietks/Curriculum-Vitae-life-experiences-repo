<![CDATA[---
title: "Developer Proposal: UnMuseum Digital Platform"
author: "Andrea Enning"
date: "28 January 2026"
mainfont: "Arial"
fontsize: 11pt
geometry: margin=2.5cm
---

# Developer Proposal: UnMuseum Digital Platform
## Black South West Network

**Submitted by:** Andrea Enning  
**Date:** 28 January 2026  
**Email:** andiekobbietks@outlook.com  
**Telephone:** +44 07480 261369  
**LinkedIn:** linkedin.com/in/andiekobbietks  
**GitHub:** github.com/andiekobbietks

---

## 1. Executive Summary

I am a first gen graduate and IT professional with deep expertise in web development, cloud infrastructure, and artificial intelligence solutions. My background uniquely combines technical proficiency with meaningful community engagement work, particularly with organisations supporting Black and racially minoritised communities.

**Why I am the right fit for the UnMuseum:**

- **Community-first approach**: Advisory roles with FirstGens CIC, Enprise/Italian Blackpreneurs, Irene Vera Foundation, and Di FELLOWS demonstrate my commitment to empowering underrepresented communities through technology
- **Rapid prototyping expertise**: I build production-ready prototypes using Lovable.dev (2.3 million users), turning ideas into functional platforms within days rather than months
- **Product leadership**: Served as Product Owner and Manager for PRGRSS (April to July 2025), a global mentorship platform under Global Purpose Enterprise, coordinating development teams across United Kingdom and Pakistan time zones
- **AI integration specialist**: My dissertation on Retrieval Augmented Generation architecture (First Class) and intensive work with fourteen AI platforms (3,800 platform interactions in eight weeks) positions me to bring cutting-edge technology to heritage preservation
- **Microsoft compliance expertise**: Successfully secured $5,000 Azure AI facility for Nyfasi through Microsoft nonprofit programme, navigating the complete verification cycle
- **Not a single point of failure**: I work collaboratively with Microsoft engineers who can review and vet my architecture, ensuring BSWN has ongoing support beyond my engagement

**Connection to this opportunity**: I was introduced to BSWN and the UnMuseum opportunity by Gary Thompson, Creative and Cultural Consultant and Film Programmer at Cables and Cameras CIC in Bristol. Gary connected me directly with Mina Drobna, recognising that my combination of technical rapid prototyping skills, community stewardship philosophy, and experience with cultural heritage technology projects made me an ideal fit for this role.

---

## 2. Technical Approach

### 2.1 Platform Architecture

I propose building the UnMuseum on **Omeka S**, a leading open-source digital heritage platform used by more than 1,000 cultural institutions worldwide. This provides Dublin Core metadata standards ensuring interoperability with global archives.

**Technology Stack:**

| Layer | Technology | Purpose |
|-------|------------|---------|
| Frontend | Next.js / React | Modern, accessible web interface |
| Backend | Node.js / Firebase | Scalable API and authentication |
| Database | PostgreSQL / Vector DB | Heritage data and AI search |
| AI Integration | RAG / LangChain / Azure Cognitive | Intelligent search and chatbot |
| Voice Preservation | ElevenLabs | Oral history voice cloning |
| Cloud | Microsoft Azure | Nonprofit credits, UK data residency |
| Security | Wazuh | Zero trust monitoring and compliance |

### 2.2 ElevenLabs Voice Preservation for Oral Histories

A critical feature for UnMuseum is preserving the voices of community elders and heritage bearers. I will implement **ElevenLabs** voice technology to:

**What ElevenLabs Enables:**

| Feature | Application for UnMuseum | Value |
|---------|-------------------------|-------|
| **Voice Cloning** | Preserve voices of community elders before they pass | Permanent heritage record |
| **Oral History Playback** | Archived stories played in original speaker's voice | Authentic community connection |
| **Text-to-Speech** | Accessibility for blind and low-vision users | WCAG compliance |
| **Multilingual Synthesis** | Stories in Somali, Arabic, Caribbean dialects | Community inclusion |
| **Interactive Guides** | AI chatbot speaks in community voices | Engaging heritage experience |

**ElevenLabs Impact Program for BSWN:**

BSWN qualifies for the **ElevenLabs Impact Program** as a cultural nonprofit:
- **12 months FREE** ElevenLabs Pro license (renewable)
- 33 million characters of voice synthesis
- Professional voice cloning capabilities
- No cost to BSWN

**Application**: I will apply on BSWN's behalf through the Impact Partnership programme.

**Source**: ElevenLabs (2025) Impact Program. Available at: https://elevenlabs.io/impact-program

### 2.3 Data Sovereignty: Self-Hosted on BSWN's Tenant

**Critical principle: BSWN owns and controls all community data.**

| Aspect | Implementation | Benefit |
|--------|---------------|---------|
| **Azure Tenant** | BSWN's own Microsoft tenant, not mine | Full data ownership |
| **UK Data Residency** | Azure UK South region | GDPR compliance |
| **Self-Hosted Database** | PostgreSQL on BSWN infrastructure | No third-party data access |
| **Backup Control** | BSWN-managed backup policies | Heritage preserved long-term |
| **Access Control** | BSWN staff as Global Admins | Complete sovereignty |

I configure the infrastructure, then **transfer full control to BSWN**. Your data never resides on my systems.

### 2.4 Security Architecture: Wazuh and Zero Trust

I will implement enterprise-grade security through **Wazuh**, an open-source security platform, ensuring BSWN has ongoing protection:

**Wazuh Security Implementation:**

| Component | Function | Benefit |
|-----------|----------|---------|
| **Intrusion Detection** | Real-time threat monitoring | Immediate alert on attacks |
| **Log Analysis** | Centralised security logging | Audit trail for NLHF |
| **Vulnerability Assessment** | Continuous scanning | Proactive risk management |
| **Compliance Monitoring** | GDPR, Cyber Essentials alignment | Funder confidence |
| **File Integrity** | Detect unauthorised changes | Heritage content protection |

**Zero Trust Architecture:**

| Principle | Implementation |
|-----------|---------------|
| Never trust, always verify | Multi-factor authentication for all users |
| Least privilege access | Role-based permissions (admin, curator, contributor, viewer) |
| Assume breach | Continuous monitoring via Wazuh |
| Explicit verification | Every access request authenticated |
| Micro-segmentation | Database isolated from public interface |

**Source**: Wazuh (2025) Open Source Security Platform. Available at: https://wazuh.com

### 2.5 Acting as Interim CIO

During the project, I will function as BSWN's **interim Chief Information Officer (CIO)**:

| CIO Responsibility | My Delivery |
|-------------------|-------------|
| Technology strategy | UnMuseum architecture aligned with BSWN mission |
| Security oversight | Wazuh implementation and monitoring |
| Vendor management | Microsoft, ElevenLabs, hosting relationships |
| Compliance | GDPR, Cyber Essentials, NLHF requirements |
| Staff training | Empower BSWN team to manage independently |
| Risk management | Business continuity and disaster recovery |

**Handover**: At project end, I document everything so BSWN can either manage internally or onboard a permanent technology lead.

### 2.6 Microsoft Engineer Review: Not a Single Point of Failure

**I am committed to ensuring BSWN is never dependent solely on me.**

| Safeguard | Implementation |
|-----------|---------------|
| **Architecture Review** | Microsoft engineers review my Azure design via Partner programme |
| **Documentation** | Comprehensive technical guides for any developer to continue |
| **Open Source** | No proprietary code that locks BSWN to me |
| **Knowledge Transfer** | BSWN staff trained on all systems |
| **Community of Practice** | Connect BSWN with other heritage technology organisations |

**Microsoft Architect Review Process:**

1. I design the UnMuseum Azure architecture
2. Submit for review through Microsoft for Startups/Nonprofit programme
3. Microsoft Solutions Architect provides feedback
4. I implement recommendations
5. BSWN receives Microsoft-vetted infrastructure

This ensures professional validation and ongoing Microsoft support relationship.

---

## 3. Work Packages and Deliverables

### Work Package 1: Discovery and Design (Weeks 1 to 4)

| Deliverable | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
| WP1.1 Community Research | Stakeholder interviews, needs assessment | Research report approved by BSWN |
| WP1.2 Wireframes | User interface designs | Sign-off from project lead |
| WP1.3 Lovable Prototypes | Interactive clickable prototypes | Community feedback collected |
| WP1.4 Microsoft Registration | BSWN nonprofit Azure tenant | Tenant active with credits |
| WP1.5 ElevenLabs Application | Impact Program application | License approved |

### Work Package 2: Core Development (Weeks 5 to 10)

| Deliverable | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
| WP2.1 Platform Foundation | Omeka S installation, Azure deployment | Platform accessible |
| WP2.2 Authentication | User registration, roles, permissions | Secure login functional |
| WP2.3 Content Management | Admin dashboard, content upload | Staff can add content |
| WP2.4 Wazuh Security | Security monitoring installation | Alerts functioning |

### Work Package 3: Feature Development (Weeks 11 to 16)

| Deliverable | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
| WP3.1 Archive System | Multimedia upload, Dublin Core metadata | Heritage items catalogued |
| WP3.2 AI Search | Vector search, semantic discovery | Relevant results returned |
| WP3.3 Voice Integration | ElevenLabs oral history playback | Voices preserved and playable |
| WP3.4 Community Features | User contributions, moderation | Community can submit stories |

### Work Package 4: Testing and Compliance (Weeks 17 to 20)

| Deliverable | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
| WP4.1 Beta Testing | Community user testing | Feedback incorporated |
| WP4.2 Accessibility Audit | WCAG 2.1 AA compliance | Audit passed |
| WP4.3 Security Review | Penetration testing, Microsoft review | Vulnerabilities addressed |
| WP4.4 GRC Documentation | Policies, procedures, compliance | NLHF requirements met |

### Work Package 5: Launch and Handover (Weeks 21 to 24)

| Deliverable | Description | Acceptance Criteria |
|-------------|-------------|---------------------|
| WP5.1 Platform Launch | Go-live, public access | Platform live |
| WP5.2 Staff Training | Admin training, documentation | Staff confident |
| WP5.3 Technical Handover | Full documentation, credentials | BSWN has complete control |
| WP5.4 Support Transition | 12-month support agreement | Support process clear |

---

## 4. Timeline and Gantt Chart

### Phase Overview

| Phase | Duration | Weeks | Key Deliverables |
|-------|----------|-------|------------------|
| Discovery and Design | 4 weeks | 1 to 4 | Research, wireframes, prototypes, Microsoft/ElevenLabs setup |
| Core Development | 6 weeks | 5 to 10 | Platform, authentication, CMS, Wazuh security |
| Feature Development | 6 weeks | 11 to 16 | Archive, AI search, voice integration |
| Testing and Compliance | 4 weeks | 17 to 20 | Beta testing, accessibility, security review |
| Launch and Handover | 4 weeks | 21 to 24 | Go-live, training, documentation |
| Support Period | 6 months | 25 to 48 | Maintenance, bug fixes, enhancements |

### Gantt Chart

```
WEEK:        1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
             |--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
DISCOVERY    [=========]
  Research      [===]
  Wireframes       [===]
  Prototypes          [===]
  MSFT/11Labs   [======]
             
CORE DEV              [==================]
  Platform               [=========]
  Auth                      [======]
  CMS                          [======]
  Wazuh                     [======]
             
FEATURES                                [==================]
  Archive                                  [=========]
  AI Search                                   [======]
  Voice                                          [======]
             
TESTING                                                   [===========]
  Beta                                                       [======]
  Access Audit                                                  [===]
  Security                                                        [===]
             
LAUNCH                                                                  [=========]
  Go-live                                                                  [===]
  Training                                                                    [===]
  Handover                                                                       [===]
```

---

## 5. Budget Breakdown

### 5.1 SFIA-Based Pricing Rationale

This pricing follows the **Skills Framework for the Information Age (SFIA)**, the industry standard for IT skills assessment used by the UK Government Digital Service and public sector procurement.

**My SFIA Level Assessment: Level 4 (Enable)**

SFIA Level 4 practitioners "work under general direction within clear framework of accountability, plan and manage their own work to meet objectives" (SFIA Foundation, 2024).

### 5.2 Detailed Cost Breakdown

| Work Package | Days | Day Rate | Cost |
|--------------|------|----------|------|
| **WP1: Discovery and Design** | 10 | £350 | £3,500 |
| Community research and consultations | 3 | £350 | £1,050 |
| Wireframes and UX design | 3 | £350 | £1,050 |
| Lovable prototypes | 2 | £350 | £700 |
| Microsoft/ElevenLabs setup | 2 | £350 | £700 |
| **WP2: Core Development** | 15 | £400 | £6,000 |
| Platform foundation (Omeka/Azure) | 5 | £400 | £2,000 |
| Authentication system | 4 | £400 | £1,600 |
| Content management | 4 | £400 | £1,600 |
| Wazuh security setup | 2 | £400 | £800 |
| **WP3: Feature Development** | 15 | £400 | £6,000 |
| Archive system | 5 | £400 | £2,000 |
| AI search integration | 5 | £400 | £2,000 |
| ElevenLabs voice integration | 3 | £400 | £1,200 |
| Community features | 2 | £400 | £800 |
| **WP4: Testing and Compliance** | 5 | £400 | £2,000 |
| Beta testing coordination | 2 | £400 | £800 |
| Accessibility audit | 1.5 | £400 | £600 |
| Security review | 1.5 | £400 | £600 |
| **WP5: Launch and Handover** | 5 | £400 | £2,000 |
| Platform launch | 1 | £400 | £400 |
| Staff training | 2 | £400 | £800 |
| Documentation | 2 | £400 | £800 |
| **Contingency (10%)** | - | - | £2,000 |
| **TOTAL** | **50 days** | - | **£21,500** |

### 5.3 Additional Value (Included at No Cost)

| Service | Market Value | My Price |
|---------|-------------|----------|
| Microsoft nonprofit onboarding | £2,000 | Included |
| ElevenLabs Impact Program application | £500 | Included |
| Azure credits secured (annual) | £2,800 | Included |
| Microsoft 365 nonprofit setup | £1,000 | Included |
| Wazuh security platform | £3,000 | Included |
| 12-month support | £4,000 | Included |
| **Total Value Added** | **£13,300** | **£0** |

### 5.4 Total Cost of Ownership (5-Year Analysis)

| Cost Category | Traditional Agency | My Model | Your Savings |
|---------------|-------------------|----------|--------------|
| Initial Development | £45,000 to £80,000 | £21,500 | £23,500 to £58,500 |
| Annual Hosting | £3,000 to £6,000 | £0 to £500 | £2,500 to £5,500 per year |
| Annual Maintenance | £8,000 to £15,000 | £2,000 to £4,000 | £6,000 to £11,000 per year |
| Microsoft 365 | £2,000 per year | £0 (nonprofit) | £2,000 per year |
| ElevenLabs | £2,640 per year | £0 (Impact Program) | £2,640 per year |
| **5-Year Total** | **£120,000 to £200,000** | **£35,000 to £50,000** | **£70,000 to £150,000** |

### 5.5 Payment Schedule

| Milestone | Percentage | Amount | Deliverable |
|-----------|------------|--------|-------------|
| Contract Signing | 20% | £4,300 | Project initiation |
| WP1 Complete | 15% | £3,225 | Research, prototypes |
| WP2 Complete | 25% | £5,375 | Core platform |
| WP3 Complete | 20% | £4,300 | Full features |
| WP4/5 Complete | 20% | £4,300 | Launch, handover |

**Business and Accountancy:**
- Business Account: Mettle (NatWest)
- Accountancy: FreeAgent (Making Tax Digital compliant)
- Invoicing: Professional invoices with full breakdown

---

## 6. Community Engagement Strategy

### 6.1 Co-Design Principles

| Principle | Implementation |
|-----------|---------------|
| **Nothing about us without us** | Community members involved in every design decision |
| **Accessible participation** | Online and in-person consultation options |
| **Multiple narratives** | Platform honours contested histories, not single story |
| **Intergenerational** | Young people and elders both represented |
| **Multilingual** | Content in community languages |

### 6.2 Engagement Activities

| Phase | Activity | Participants |
|-------|----------|--------------|
| Discovery | Community listening sessions | 20 to 30 community members |
| Design | Wireframe review workshops | 10 to 15 representatives |
| Prototyping | Click-through testing | 5 to 10 diverse users |
| Development | Feature feedback sessions | Ongoing community panel |
| Beta | User acceptance testing | 20 to 30 beta testers |
| Launch | Celebration event | Wider community |

### 6.3 Voice Preservation Programme

**ElevenLabs-powered oral history initiative:**

1. Identify community elders and heritage bearers
2. Record high-quality voice samples (supervised, consented)
3. Create voice clones for archival purposes
4. Enable future generations to hear stories in original voices
5. Provide accessibility through text-to-speech in community voices

---

## 7. Managed Service Commitment

### My Commitment to BSWN for Your Funding Duration

I am committed to supporting BSWN throughout the full duration of your National Lottery Heritage Fund grant period:

**During the Project (Months 1 to 12):**
- Full development and delivery
- Weekly progress reports
- Responsive communication within one working day

**Post-Launch Support (Months 13 to 24):**
- Included maintenance and bug fixes
- Staff training refreshers
- Microsoft grant renewal assistance

**Extended Partnership (Years 2 to 4):**
- Priority access for additional work
- Ongoing digital strategy advisory
- Grant application support
- Technology roadmap planning

**My commitment**: I do not deliver a platform and disappear. I build lasting relationships because community technology requires sustained partnership.

---

## 8. Professional Experience and References

### 8.1 Relevant Experience

**PRGRSS / Global Purpose Enterprise: Product Owner and Manager**  
April to July 2025 | United Kingdom to Pakistan Coordination

- Led product development for global mentorship platform
- Managed cross-timezone development team
- Built four rapid prototypes using Lovable.dev
- Reduced development miscommunication by 60 per cent

**Nyfasi: Microsoft Nonprofit Onboarding**  
September 2020 to December 2020

- Secured $5,000 Azure AI facility through Microsoft nonprofit programme
- Navigated complete Microsoft compliance verification cycle
- Demonstrated exact skills needed for BSWN onboarding

**University of South Wales: Digital Technical Mentor**  
September 2023 to August 2024

- Supported 23,000 users across multiple campuses
- Enterprise IT support and training delivery

**Technocamps: STEM Ambassador**  
February 2023 to August 2024

- Wales-wide education delivery
- Ukrainian refugee children technology workshops

### 8.2 Qualifications

- **BSc (Hons) ICT** | University of South Wales (2:1, Dissertation: First Class)
- **AWS Cloud Engineering re/Start** | Cardiff and Vale College (2024)
- **DBS Enhanced Check** | Cleared

### 8.3 References

Available upon request from:

- **Gary Thompson** | Creative and Cultural Consultant, Cables and Cameras CIC, Bristol
- **Laura Roberts** | Technocamps, Wales
- **Sally-Anne** | USW Study Skills Team
- **Alaya** | CEO, FirstGens CIC
- **Hope** | Founder, Irene Vera Foundation

---

## 9. Closing Statement

The UnMuseum is an extraordinary opportunity to create something truly meaningful: a living digital space where Black and racially minoritised communities across the South West can see themselves, tell their own stories, and preserve their heritage for future generations.

I bring:
- Technical excellence proven across multiple platforms
- Microsoft nonprofit expertise (demonstrated with Nyfasi)
- ElevenLabs voice preservation for oral histories
- Enterprise security through Wazuh
- Zero trust architecture ensuring data protection
- Commitment to knowledge transfer so BSWN is never dependent solely on me
- Microsoft engineer review ensuring professional validation

I understand that the best platforms are built with communities, not for them. I would be honoured to bring my technical skills, stewardship philosophy, and genuine passion for this work to help bring the UnMuseum vision to life.

**Let us build something powerful together.**

**Andrea Enning**  
28 January 2026

---

*Submitted to: Mina Drobna, Operations Director*  
*Email: mina@bswn.org.uk*

---

## Bibliography

ElevenLabs (2025) *Impact Program*. Available at: https://elevenlabs.io/impact-program (Accessed: 28 January 2026).

Heritage Fund (2024) *Good Practice Guidance: Digital Projects*. National Lottery Heritage Fund. Available at: https://www.heritagefund.org.uk (Accessed: 28 January 2026).

Microsoft (2019) 'Breaking New Sound: The Hip Hop Museum', *Microsoft Unlocked*. Available at: https://unlocked.microsoft.com/the-hip-hop-museum/ (Accessed: 28 January 2026).

Microsoft (2024) 'Microsoft for Nonprofits: Eligibility', *Microsoft Nonprofits*. Available at: https://www.microsoft.com/en-us/nonprofits/eligibility (Accessed: 28 January 2026).

Omeka (2025) *Omeka S Technical Documentation*. Available at: https://omeka.org (Accessed: 28 January 2026).

SFIA Foundation (2024) *SFIA 9: Skills Framework for the Information Age*. Available at: https://sfia-online.org (Accessed: 28 January 2026).

Wazuh (2025) *Open Source Security Platform*. Available at: https://wazuh.com (Accessed: 28 January 2026).
]]>