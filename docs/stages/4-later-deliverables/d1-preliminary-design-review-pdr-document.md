---
title: "Preliminary Design Review (PDR) Document"
stage: "Later Deliverables"
deliverable_id: stage4-d1
status: draft
last_reviewed: 2026-05-23
---

# Preliminary Design Review (PDR) Document

Stage 3 — Synthesis

**0.0 Introduction**

A design review evaluates a design against its requirements to **verify previous work** and **identify issues** before committing to further development. It must involve reviewers external to the design team. Because the cost of correcting a fault grows as development progresses, early reviews are a high-value investment.

This document demonstrates that the preliminary design meets all system requirements with acceptable risk and within cost and schedule constraints, and establishes the basis for proceeding with detailed design. It confirms that the correct design options have been selected, interfaces identified, and verification methods defined.

The structure follows Preliminary Design Review (PDR) conventions as described in the Auburn University systems engineering curriculum, consistent with DoD and NASA PDR practice. Each section corresponds to a distinct stage of the synthesis process and maps to one or more Stage 3 deliverables.

**Purpose of this document**

The purpose of the PDR is to **review the** **conceptual design** to ensure that the planned technical approach will meet the requirements.

The following are typical objectives of a PDR:

- Ensure that all system requirements have been validated, allocated, the requirements are complete, and the flowdown is adequate to verify system performance

- Show that the proposed design is expected to meet the functional and performance requirements

- Show sufficient maturity in the propos**Preliminary Design Review Document**ed design approach to proceed to final design

- Show that the design is verifiable and that the risks have been identified, characterized, and mitigated where appropriate.

**1.0 Functional architecture**

This section presents how the selected system concept was transformed into a functional architecture. It covers the decomposition of high-level actions into subsystem-level behaviours, the identification of interfaces between subsystems, and the construction of the Physical I/O and Asset diagrams that form the basis for requirements generation.

### **1.1 Subsystem decomposition** 

**➤** 1.1.1 Briefly describe the subsystem structure with how many subsystems the system has, what each one is responsible for, and the overall operational logic that connects them.

*Note: This narrative should be written for an industry reviewer who has not seen your Innoslate model.*

### **1.2 Low-level action diagrams**

The low-level action diagrams decompose the high-level action diagram from Stage 1 to a level where individual subsystems can be assigned responsibility for each action. Decomposition continues until actions can be implemented by hardware, software, or people.

**➤** 1.2.1 Present the low-level action diagrams for each high-priority use case. For each diagram:

- Embed the diagram image exported from Innoslate.

- Provide a figure caption identifying the use case and the scenario.

- Include a one to two sentence description beneath the figure explaining what the diagram shows and which subsystems are most active in this scenario.

*Note: If diagrams exist for multiple scenarios of the same use case, group them together.*

### **1.3 Physical I/O and asset diagram** 

The Physical I/O Diagram integrates the functional model (action diagrams) with the physical model (subsystems and assets) into a single connected representation.

**➤** 1.3.1 Present the top-level Physical I/O Diagram showing all subsystem assets and external entities, with conduits connecting them. For each:

- Embed the diagrams with figure captions.

- Add decomposition diagrams for any subsystem that is itself composed of sub-assets.

- After the Physical I/O Diagram, include a brief interface summary table identifying each conduit, the subsystems it connects, and the type of flow (information, energy, or material).

**➤** 1.3.2 Present the top-level Asset Diagram generated from the Physical I/O Diagram. For each diagram:

- Embed the diagram with figure captions.

- Add decomposition diagrams for any subsystem that is itself composed of sub-assets.

*Note: If subsystem-level decomposition diagrams exist for complex assets, include them as sub-figures immediately after the top-level diagram.*

## **2.0 Requirements baseline**

This section presents the formal requirements baseline established during Stage 3. The primary document is the System Requirements Document (SRD), which contains three integrated layers: functional requirements (SRD Section 3.2, corresponding to Deliverable 3), technical requirements derived from the trade studies, and verification requirements (SRD Section 4, corresponding to Deliverable 6).

### **2.1 Completing the SRD**

The SRD is generated from the Asset Diagram using the Generate SRD function in Innoslate. This auto-populates sections that are directly traceable to the model.

**➤** 2.1.1 Populate the following sections in SRD manually to the extent possible given the current state of component selection:

- Section 3.1 — Required states and modes: identify each distinct operational mode (standby, active, emergency, maintenance) and note which Section 3.2 requirements apply in each mode.

- Section 3.6 — Adaptation requirements: installation-dependent parameters and operational variables.

- Section 3.7 — Safety requirements: hazardous conditions, fail-safe behaviours, required interlocks. If no hazardous elements exist, state this explicitly.

- Section 3.8 — Security and privacy requirements: protection mechanisms, threats, applicable regulations.

- Section 3.9 — System environment requirements: temperature, humidity, shock, vibration, electromagnetic environment, and storage and transportation conditions.

- Section 3.11 — System quality factors: reliability (MTBF), availability (uptime), maintainability (MTTR), testability, and usability — all stated quantitatively where possible.

- Section 3.12 — Design and construction constraints: mandatory architecture choices, physical limits, material restrictions, applicable standards.

- Sections 3.13 to 3.18 — Personnel, training, logistics, packaging, statutory requirements: complete as applicable to the system.

- Sections 3.10 — Computer resource requirements

**➤** 2.1.2 Provide a brief narrative describing the key requirements from 2.1.1. Focus on explaining the intent and context behind the requirements rather than listing them verbatim. The full set of requirements will be documented in Appendix A.

### **2.2 Functional and Technical Requirements**

**➤** 2.2.1 Provide a brief narrative describing the key functional and technical requirements for each major subsystem in your design, and explain the rationale or the approach used to derive the requirements.

**➤** 2.2.2 Add the complete SRD in Appendix A. Add the full derivation of technical requirements in Appendix B.

**2.3 Open Requirements**

**➤** 2.3.1 List the requirements belonging to major or primary subsystems that are not specified as yet in the SRD. For each open item, identify the requirement ID and the information needed to resolve it.

*This list signals to the panel where the requirements baseline is still maturing.*

## **3.0 Technology selection and derivation**

This section covers the two-stage trade study process that translates subsystem functional requirements into specific component selections. The goal is to demonstrate that components were selected against those derived requirements, not by familiarity or convenience.

The process proceeds in two stages:

1.  **Technology Class Selection (Deliverable 4):** What type of technology can perform this function, and what technical parameters must it meet?

2.  **Component Selection (Deliverable 7):** Which specific product within that technology class best meets the derived specifications?

The outputs of both stages feed into quantitative thresholds that make Section 3.2 requirements verifiable, and component-level data needed for budget rollups.

### **3.1 Technology class trade studies**

**➤** 3.1.1 Summarise the key technical requirements that drove the technology class selection for each subsystem. For each subsystem, briefly state the functional requirement being addressed, the governing technical parameter, and the final specified value. Attach the full derivation working in Appendix B.

**➤** 3.1.2 For each subsystem, summarise the outcome of the technology class comparison, identifying the selected technology class and the key reasons for its selection.

**➤** 3.1.3 Summarise the key technology class risks identified during Deliverable 4 and their association with the technology selection decision. Do not reproduce the full risk details here — attach the complete risk documentation in Appendix C.

*Remember! The review panel needs to see the analytical chain — from functional requirement to technical parameter to evaluated technology classes to selected class — not just the conclusion.*

### **3.3 Component selection trade studies**

**➤** 3.3.1 For each subsystem, summarise the outcome of the component evaluation, highlighting which candidates met the selection criteria and which did not. Do not reproduce the full evaluation table here — attach the complete component evaluation table in Appendix B.

**➤** 3.3.2 Summarise the key component-level risks identified during Deliverable 7, including supply chain, obsolescence, integration, and environmental compliance risks, in the context of the component selection they are associated with. Do not reproduce the full risk details here — attach the complete risk documentation in Appendix C.

## **4.0 Performance analysis**

This section presents the system-level analyses conducted to confirm that the chosen architecture is viable as a whole. Where the component evaluation tables in Section 3 confirm that individual parts meet individual requirements in isolation, this section shows that the integrated system meets its top-level constraints.

### **4.1 Analyses**

**➤** 4.1.1 Present a summary of each of the analyses performed and their key results, including traditional and domain-specific analyses. Include the details in Appendix C.

## **5.0 Verification approach**

This section presents the verification requirements established in SRD Section 4. For each system requirement, there is a corresponding verification requirement that specifies the method by which compliance will be confirmed and the acceptance criterion that defines a passing result. The full verification requirements are in Appendix A (SRD).

**4.1 Verification methods**

For each requirement in the **Requirements Baseline** section, provide a brief narrative description of how the requirements will be verified — the methods used and the reasoning behind them. Detailed verification requirements are in Appendix A as part of the SRD.

### **4.2 Verification traceability**

Include the verification traceability matrix exported from Innoslate, showing each system requirement linked to its verification requirement(s). This confirms that every requirement has a verification path. Include the matrix in full here in Appendix E.

### **4.3 Notable verification considerations**

Identify any verification requirements that will require special equipment, facilities, access, or scheduling arrangements to execute. These are constraints on the build and test plan and should be visible to the panel before Section 6 is presented.

##  

## **6.0 Risk register**

This section consolidates the risks identified across the three analytical deliverables of Stage 3. Risks are presented in three layers reflecting the order in which they were discovered during the synthesis process. The risk register must be consistent with the Risk entities recorded in Innoslate.

### **6.1 Layer 1 — Technology class risks (from Deliverable 4)**

Present the risks identified when evaluating which type of technology could perform each subsystem function. These risks relate to the operating principle and supply characteristics of a technology class, not to any specific product. Typical technology class risks include:

- Performance risk: does the technology class meet the final specified value under the worst-case scenario, or only under nominal conditions?

- COTS or GOTS dependency: is the class dominated by a small number of suppliers or subject to export restrictions?

- Integration risk: does the class require specialised drivers, calibration equipment, or interface standards that could create compatibility issues?

- Environmental risk: does the class perform reliably across the full operating range defined in SRD Section 3.9?

### **6.2 Layer 2 — Component risks (from Deliverable 7)**

Present the risks identified when selecting specific components within the chosen technology class. Typical component risks include:

- Supply chain risk: single-source dependency, distributor availability, or extended lead times.

- Obsolescence risk: end-of-life products or recently released components with an unproven supply history.

- Performance risk: datasheet performance reported under nominal conditions that may not hold under worst-case operating conditions.

- Environmental compliance risk: component rated operating range narrower than the system environment requirement.

### **6.3 Layer 3 — System-level risks (from Deliverable 8)**

Present the risks that emerged from the performance analysis and reflect uncertainties at the level of the integrated system. These include:

- Budget margin risks: any mass, power, or cost budget with a yellow or red margin.

- Timing risks: scenarios where the Monte Carlo simulation shows a meaningful probability of failing the timing requirement.

- Analysis assumption risks: system-level analyses that relied on assumptions that may not hold in the actual operating environment.

### **6.4 Risk summary table**

Present a consolidated risk summary table for all risks rated medium or above, drawn from all three layers. The table should include, for each risk: a unique Risk ID (cross-referencing the Innoslate entity), a brief description, the layer it originated from, the likelihood and consequence ratings, and the mitigation strategy.

### **6.5 Risk summary table**

The following table should be completed for all risks rated medium or above. Risks rated low may be noted in the Innoslate risk chart without requiring a row in this table.

| **Risk ID** | **Description** | **Layer** | **Rating (L/C)** | **Mitigation** |
|----|----|----|----|----|
|  | Enter risk description | 1 / 2 / 3 | L: H/M/L C: H/M/L | Enter mitigation strategy |
|  |  |  |  |  |
|  |  |  |  |  |

## **7.0 Build and verification plan**

The plan describes how the team will build, integrate, and verify the system from the current state through to final demonstration. It converts technical decisions into a structured execution plan: risks from Section 6 become early-phase mitigation tasks, verification requirements from Section 4 become gate criteria, and the BOM from Section 5 drives the procurement schedule.

### **7.1 Plan structure overview**

Open with a brief narrative (three to five sentences) describing the overall plan structure: how many phases the plan has, the total duration, and the major gate events. This orients the panel to the plan before they examine the detail.

### **7.2 Level 1 phase plan**

Present the Level 1 phase plan. For each phase, include:

- The macro-deliverables produced in that phase, each stated as an output rather than an activity.

- The gate criteria that must be met before proceeding to the next phase, referenced to specific verification requirements in SRD Section 4.

- The planned start and end dates and the team members responsible.

The Level 1 plan should be presented as a Gantt view exported from the project plan template, with phase boundaries and gate events clearly visible.

### **7.3 Level 2 iteration plan**

Present a summary of the Level 2 sprint structure for each phase. For each phase, identify:

- The high-risk and high-uncertainty items placed at the front of the phase.

- Long-lead procurement items and their planned procurement dates.

- The gate review preparation sprint, placed one to two weeks before the end of the phase.

The full Level 2 plan is included as Appendix D. In this section, present a condensed view covering the most significant mid-level deliverables and dependencies per phase.

## **Appendices**

The appendices contain the full artifacts referenced in the main body. Each section of the main body is designed to be readable without opening the appendices. The appendices allow a reviewer to examine the detail behind any claim in the main body.

### **Appendix A — System Requirements Document (SRD)**

The full SRD exported from Innoslate, including all sections completed during Stage 3. This document captures the functional requirements (SRD Section 3.2), all technical requirements, and the verification requirements (SRD Section 4). Export as a Basic Document Output (DOCX) from Innoslate.

Also include the following traceability matrices exported from Innoslate:

- Stakeholder requirements to system requirements matrix.

- System requirements to verification requirements matrix.

### **Appendix B — Trade study tables (Deliverables 4 and 7)**

The complete trade study documentation, including:

- Literature review summaries for each subsystem function.

- Technical Requirements Tables with full derivation working (Deliverable 4).

- Technology class comparison tables or Pugh matrices.

- Component evaluation tables with candidate datasheets (Deliverable 7).

- Decision records for each technology class and component selection.

### **Appendix C — Design analysis report and BOM (Deliverable 8)**

The full Design Analysis Report from Deliverable 8, including:

- Analysis plan table.

- Budget analysis working for all applicable constraints.

- Discrete event simulation results and Monte Carlo histograms.

- Domain-specific analysis results where applicable.

- Full Bill of Materials compiled using the BOM template.

### **Appendix D — Project plan (Deliverable 9)**

The completed project plan Excel file, including the full Level 1 and Level 2 plans for all components. Export or print as a PDF showing the Gantt view with all rows visible.

### **Appendix E — Traceability matrices**

The following matrices exported from Innoslate to demonstrate end-to-end traceability across Stage 3:

- System requirements to component assets (satisfied by): confirms every technical requirement is satisfied by at least one selected component.

- Component assets to actions (performs): confirms every leaf-level action in the action diagram is allocated to a component asset.

- Requirements to risks: confirms that safety-critical and performance-critical requirements have associated risk analysis.

relationships guidelines

**LML Relationship Correction & Traceability Matrix Guidelines**

Spring 2026 \| Habib University

## **1. Purpose and Scope**

This document provides two sets of guidelines to help you review and improve your Innoslate model.

- Section 2 cross-references every LML relationship name explicitly instructed in the ASEPD deliverables document against LML Specification 2.0, identifies errors and non-standard usage, and gives the correct verb to use instead.

- Section 3 defines which traceability matrices to generate, what entity pairs each matrix covers, and the minimum population thresholds required for a model to be considered reviewable.

These guidelines apply to all three gate stages: Requirements (Gate 2), System Concept (Gate 3), and Initial System Architecture (Gate 4).

> **Note:** All relationship names in LML are bidirectional. The table in Section 2 always states the relationship from the perspective of the first entity in the pair (the source). The inverse is implied.

## **2. LML Relationship Review by Deliverable**

The table below lists every entity pair for which the ASEPD deliverables document instructs a specific relationship name. Each entry is evaluated against LML Specification 2.0 and assigned one of three verdicts:

| **✅ Correct** | Relationship is valid in base LML 2.0 for this entity pair. | **❌ Incorrect** | Relationship does not exist or direction is wrong in LML 2.0. | **⚠️ Caution** | Relationship exists only in the SysML extension (Appendix A) or semantics are weak. |
|----|----|----|----|----|----|

??? note "Sadaf · 2026-05-21"
    modify for version LML 1.4 because I later found that Innoslate employs LML 1.4
<!-- comment:29 -->


> **Stage 1— Requirements Stage**

| **Deliverable** | **Entity Pair (Source → Target)** | **Instructed Verb** | **Verdict** | **Correct Entity Pair** | **Correct LML 1.4 Verb** | **Explanation / Action Required** |
|----|----|----|----|----|----|----|
| Raw Evidence(Del. 1) | Notes Document → Raw Artifact | **"related to"** | **✅ Correct** |  |  | Relationships that exist between two artifacts are: “related to” and “decomposed by”. Out of the two, “related to” is more appropriate. |
| User Needs(Del. 1) | Statement (UN.1.n) → Statement (Notes Document) | **"traced to"** | **✅ Correct** |  |  | LML §3.4.0.2.13 defines traced from/traced to between Statements. Direction is correct: a refined UN Statement is traced to its source Statement in the Notes Document. |
| Stakeholder Req.(Del. 3) | Requirement (SR) → Statement (UN) | **"traced from"** | **❌ Incorrect** |  | "traced to" | LML §3.4.11.3 and Fig. 3-1 confirm: Requirement traced from Statement is the primary requirements traceability path. No change needed. |
| Stakeholder Req.(Del. 3) | Requirement (SR) → Issue entity | **"causes"** | **✅ Correct** |  |  | LML §3.4.0.2.1 defines causes specifically toward a Risk entity. Since the issue is modelled as a Risk entity, causes is correct. If modelled as a Decision, use results in instead. |
| Stakeholder Req.(Del. 3) | Trade Study (Artifact) → Issue/Risk | **"resolves"** | **⚠️ Caution** | Decision → Risk | "resolves" | **Replace relationship between trade study and risk with decision and risk.** It is the decision that resolves the risk. Resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Risk, and Decision enabled by Trade Study. |
| Stakeholder Req.(Del. 3) | Decision → Trade Study (Artifact) | **"enabled by"** | **✅ Correct** |  |  | LML §3.4.0.2.3 defines enables/enabled by toward Decision. The direction here is correct: Decision enabled by Trade Study Artifact. Ensure the relationship is created on the Decision entity pointing to the Artifact, not the reverse. |
| High-level Action Diagrams(Del. 4) | Action → Requirement | **"satisfies"** | **❌ Incorrect** |  | "traced to" | satisfies does not exist in base LML 2.0 (Table 3-3). |
| Verif. Req.(Del. 5) | Characteristic → Verif. Requirement | **"specifies"** | **✅ Correct** |  |  | LML §3.4.4.2 and §3.4.0.2.12 confirm: Characteristic specifies a Requirement or Verification Requirement. Direction and entity types are correct. |
| Verif. Req.(Del. 5) | Verif. Requirement → Decision | **"enables"** | **✅ Correct** |  |  | LML §3.4.0.2.3 defines enables/enabled by toward Decision. Direction is correct: Verification Requirement enables Decision. No change needed. |
| Verif. Req.(Del. 5) | Verif. Requirement → Issue/Risk | **"causes"** | **✅ Correct** |  |  | LML §3.4.0.2.1 defines causes specifically toward a Risk entity. Since the issue is modelled as a Risk entity, causes is correct. If modelled as a Decision, use results in instead. |
| Verif. Req.(Del. 5) | Verif. Requirement → Test Case | **"verified by"** | **✅ Correct** |  |  | LML §3.4.11.4.2 explicitly defines verifies/verified by between Verification Requirement and Test Case. This is correct. Ensure the relationship direction is verified by placed on the Verification Requirement pointing to the Test Case. |

??? note "Sadaf · 2026-05-21"
    there should be downstream relationships emanating from the decision (could be an asset or requirement or action) need to make fixes in guidelines to incorporate this
<!-- comment:34 -->


> **Stage 2 — System Concept Stage**

| **Deliverable** | **Entity Pair (Source → Target)** | **Instructed Verb** | **Verdict** | **Correct LML 2.0 Verb** | **Explanation / Action Required** |
|----|----|----|----|----|----|
| System Req.(Del. 3) | System Requirement → Stakeholder Requirement | **"refines" or "satisfies"** | **❌ Incorrect** | "traced to" | Neither refines nor satisfies exists in base LML 2.0 Table 3-3. The correct verb is traced from: System Requirement traced from Stakeholder Requirement. This is the same traceability verb used for Stakeholder Requirements tracing to User Needs. Using different verbs for the same traceability pattern breaks the chain. |
| System Req.(Del. 3) | System Requirement → Decision | **"enabled by"** | **✅ Correct** | "enabled by" (correct) | LML §3.4.0.2.3 defines this correctly. The Decision that drove the system requirement enables it. Ensure the relationship is created on the Requirement entity, pointing to the Decision. |
| System Req.(Del. 3) | System Requirement → Trade Study (Artifact) | **"derived from"** | **❌ Incorrect** | ”sourced by” | derived from does not exist in base LML 2.0. The correct relationship between a Requirement and a supporting Artifact is references / referenced by (§3.4.0.2.8): Requirement references Trade Study Artifact. This captures that the artifact informs the requirement without implying derivation, which is not an LML concept. |
| Verif. Req. forSystem Req. | Verif. Requirement → System Requirement | **"verifies"** | **✅ Correct** |  | LML §3.4.11.4.2 defines verifies/verified by. This is correct and consistent with the Gate 2 approach. Ensure this relationship is created for every system requirement, not just selected ones. |

> **Stage 3 — Initial System Architecture Stage**

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr>
<th><strong>Deliverable</strong></th>
<th><strong>Entity Pair (Source → Target)</strong></th>
<th><strong>Instructed Verb</strong></th>
<th><strong>Verdict</strong></th>
<th><strong>Correct LML 2.0 Verb</strong></th>
<th><strong>Explanation / Action Required</strong></th>
</tr>
<tr>
<th><p>Low-level Action Diagrams</p>
<p>(Del. 1)</p></th>
<th>Asset → Action</th>
<th><strong>"performs"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.1.2.3 defines performed by / performs. Asset performs Action is the canonical functional allocation relationship. Correct.</th>
</tr>
<tr>
<th><p>Low -level Action Diagrams</p>
<p>(Del. 1)</p></th>
<th>Action → Action (decomposition)</th>
<th><strong>"decomposes"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.0.2.2 defines decomposed by / decomposes. Parent Action decomposed by child Action is standard. Correct.</th>
</tr>
<tr>
<th>Physical I/O(Del. 2)</th>
<th>I/O entity → Conduit</th>
<th><strong>"transferred by"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.5.3.2.2 defines transfers / transferred by between Conduit and Input/Output. The direction here (I/O transferred by Conduit) is correct.</th>
</tr>
<tr>
<th>Physical I/O(Del. 2)</th>
<th>Asset → Asset (hierarchy)</th>
<th><strong>"decomposed by"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>Standard LML §3.4.0.2.2. Parent Asset decomposed by child Asset establishes subsystem hierarchy. Correct.</th>
</tr>
<tr>
<th>Subsystem Req. (Del. 5)</th>
<th>Subsystem Req → System Req</th>
<th><strong>Direct relationship doesnt exist.</strong></th>
<th style="text-align: center;"></th>
<th>“traced to”</th>
<th>Use SRD to create relationship between subsystem requirements and system requirements.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Trade Study (Artifact) → Subsystem Requirement</th>
<th><strong>"satisfies"</strong></th>
<th style="text-align: center;"><strong>❌ Incorrect</strong></th>
<th>"sourced by”</th>
<th>As noted for Del. 7 high-level actions: satisfies is not in base LML 1.4.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Issue/Risk → Trade Study (Artifact)</th>
<th><strong>"caused by"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.10.2 confirms: Risk caused by other entities, and other entities cause Risk. If the Issue is a Risk entity, caused by from the Risk to the Artifact is valid. Correct.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Decision → Trade Study (Artifact)</th>
<th><strong>"enabled by"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>Consistent with Stage 1 and Stage 2 usage. LML §3.4.0.2.3. Correct.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Measure → Requirement</th>
<th><strong>"specified by"</strong></th>
<th style="text-align: center;"><strong>❌ Incorrect</strong></th>
<th>"specifies" placed on Requirement(direction is inverted)</th>
<th>In LML §3.4.0.2.12, specified by is placed on the entity being described, pointing to the Characteristic / Measure. The deliverables document instructs placing the relationship on the Measure entity, which reverses the direction. Corrective action: open each Requirement entity, go to Relationships, and create specified by pointing to the Measure — not the other way around.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Risk → Trade Study (Artifact)</th>
<th><strong>"related to"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.0.2.9 defines related to as a generic peer-to-peer link. It is valid here, though references would be more semantically precise (the Risk is informed by the artifact). Either is acceptable.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Risk → Requirement</th>
<th><strong>"traced from"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.0.2.13 allows traced from across entity classes. A Risk entity traced from a Requirement captures that the risk is tied to that requirement's achievement. Correct.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Decision (mitigation) → Risk</th>
<th><strong>"resolves"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.0.2.10 defines resolves / resolved by: a Decision resolves a Risk. This is the correct pattern for documenting mitigation decisions. Correct.</th>
</tr>
<tr>
<th>Component TradeStudies (Del. 7)</th>
<th>Component Asset → Subsystem Asset</th>
<th><strong>"decomposed by"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>Standard asset hierarchy decomposition (§3.4.0.2.2). Subsystem Asset decomposed by Component Asset. Correct.</th>
</tr>
<tr>
<th>Component TradeStudies (Del. 7)</th>
<th>Component Asset → Action</th>
<th><strong>"performs"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>LML §3.4.1.2.3. Correct and consistent with granular action diagram allocation. Must be explicitly set — Innoslate does not propagate this from parent assets.</th>
</tr>
<tr>
<th>Component TradeStudies (Del. 7)</th>
<th>Risk → Component Asset</th>
<th><strong>"related to"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>See note above for Trade Studies (Del. 4 &amp; 7). Valid generic link. Acceptable.</th>
</tr>
<tr>
<th>Verif. Req. forSubsystem Req.</th>
<th>Verif. Requirement → Subsystem Requirement</th>
<th><strong>"verifies"</strong></th>
<th style="text-align: center;"><strong>✅ Correct</strong></th>
<th></th>
<th>Consistent with Gate 2 and Gate 3. LML §3.4.11.4.2. Correct.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

??? note "Sadaf · 2026-05-21"
    add some explanation/context
<!-- comment:39 -->


??? note "Sadaf · 2026-05-21"
    add after this: issue "references" Analysis Artifact called "Design Analysis Report"
<!-- comment:38 -->


??? note "Sadaf · 2026-05-21"
    component asset "references" trade study
<!-- comment:37 -->


??? note "Sadaf · 2026-05-21"
    Action uses Resource
<!-- comment:35 -->


??? note "Sadaf · 2026-05-21"
    Invert this so students are not confused when comparing with the deliverable guidelines
<!-- comment:32 -->


## **3. Traceability Matrix Guidelines**

### **3.1 Why Traceability Matrices Matter for Review**

A traceability matrix is a two-dimensional table that confirms every entity in one class is connected to at least one entity in another class through a specific LML relationship. Matrices serve three purposes:

- Completeness check: every row and every column must have at least one cell populated. Sparse rows or columns signal missing relationships, not missing content.

- Correctness check: the relationship verb used to generate the matrix must match the LML 2.0 standard — this is why Section 2 matters before you generate matrices.

- Coverage check: the population density of the matrix indicates whether the engineering work is superficial (one link per row) or thorough (multiple supporting links).

### **3.2 Required Matrices by Gate**

The following table defines the matrices that must be generated, and the LML relationship that drives each one..

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><strong>Matrix Name</strong></th>
<th><strong>Row Entity (source)</strong></th>
<th><strong>Column Entity (target)</strong></th>
<th><strong>LML Relationship</strong></th>
<th><strong>Review Purpose</strong></th>
<th><strong>How to Create</strong></th>
</tr>
<tr>
<th colspan="5"><strong>Stage 1 — Requirements Stage</strong></th>
<th></th>
</tr>
<tr>
<th><strong>Stakeholder Req. to User Needs</strong></th>
<th>Requirement (SR)</th>
<th>Statement (UN)</th>
<th><strong>traced to</strong></th>
<th>Confirms every stakeholder requirement traces to at least one user need. Orphan requirements (no column link) are ungrounded and likely invented. Multiple SR rows tracing to the same UN column indicate requirements that may need merging.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field.</p></li>
<li><p>Enter “class:Requirement order:number number:SR.* class:Requirement”.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter “order:number number:UN.* class:Statement”.</p></li>
<li><p>Set Relationship to “traced to”.</p></li>
<li><p>Review traces.</p></li>
<li><p>Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>High Level Actions/Scenarios to High Level Stakeholder Functional Req.</strong></th>
<th>Action</th>
<th>Requirement (SR)</th>
<th><strong>traced to</strong></th>
<th>Confirms every scenario traces to atleast one stakeholder requirement. We're doing it earlier because at this stage of the project you hadn’t yet decomposed into system requirements, and we want you to verify your functional model has coverage before that decomposition.</th>
<th><p>1. Follow the steps 1-6 in Section 3.4.</p>
<p>2. Select Query in Yaxis field and enter query:</p>
<p><strong>order:modified is:top class:Action</strong></p>
<p>3. Press “Update”</p>
<p>4. Under "Top (X Axis)" enter the query:</p>
<p><strong>order:number number:SR.* class:"Requirement" label:"Functional Requirement"</strong></p>
<p>5. Set Relationship to "traced to".</p>
<p>6. Review traces and save Matrix.</p>
<p>This gives the top level actions from all the action diagrams created.</p></th>
</tr>
<tr>
<th><strong>Verif. Req. to Stakeholder Req.</strong></th>
<th>Verif. Requirement (VR.1)</th>
<th>Requirement (SR)</th>
<th><strong>verifies</strong></th>
<th>Confirms every stakeholder requirement has a verification path. Any SR column with no populated cell means that requirement cannot be objectively proven — it must either be made verifiable or removed.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “VR.1” and select the Stakeholder Verification Requirements Document. Make sure this document has just the Verification Requirements.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter the query:<br />
query:</p></li>
</ol>
<p><strong>order:number number:SR.* class:"Requirement"</strong></p>
<ol start="6" type="1">
<li><p>Set Relationship to “verifies”.</p></li>
<li><p>Review traces.</p></li>
<li><p>Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th colspan="5"><strong>Stage 2 — System Concept Stage</strong></th>
<th></th>
</tr>
<tr>
<th><strong>System Req. to Stakeholder Req.</strong></th>
<th>Requirement (SysReq)</th>
<th>Requirement (SR)</th>
<th><strong>traced to</strong></th>
<th>Confirms every system requirement is grounded in a stakeholder requirement. Any SysReq row with no SR column link is a gold-plated requirement (added without stakeholder basis). Columns with no row link indicate stakeholder requirements not yet decomposed into system requirements.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “SYS.1” and select the System Requirements Document. Make sure this document has just the System Requirements.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SR.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “traced to”.</p></li>
<li><p>Review traces.</p></li>
<li><p>Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>System Functional Req. to Scenarios</strong></th>
<th>Requirement (SysReq)</th>
<th>Action</th>
<th><strong>traced to</strong></th>
<th>Confirms every system functional requirement is traced to a scenario. In other words, it confirms that every operational scenario can be executed by the architecture.</th>
<th><p>1. Open the top-level action diagram.</p>
<p>2. Open the Hierarchy or Tree diagram to review the traces between functional requirements/actions and scenarios.</p></th>
</tr>
<tr>
<th><strong>Verif. Req. to System Req.</strong></th>
<th>Verif. Requirement (VR.2)</th>
<th>Requirement (SysReq)</th>
<th><strong>verifies</strong></th>
<th>Confirms every system requirement has a verification path. System requirements are solution-dependent and more specific — most should be directly verifiable. Columns with no row link must be addressed before Gate 3 approval.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “VR.2” and select the System Verification Requirements Document. Make sure this document has just the Verification Requirements.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SYS.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “verifies”.</p></li>
<li><p>Review traces and Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Risks to Requirements</strong></th>
<th>Risk</th>
<th>Requirement (SR or SysReq)</th>
<th><strong>caused by</strong></th>
<th>Confirms that identified risks are anchored to specific requirements whose achievement they threaten. A Risk entity with no requirement link is floating and cannot be prioritised. A requirement with many Risk links is a signal of high-risk scope that warrants trade study attention.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field.</p></li>
<li><p>In Query field, type “order:modified- class:Risk”</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “Stakeholder Requirements Document” for Stakeholder Requirements and “System Requirements Document” for System requirements, respectively in Root Entity.</p></li>
<li><p>Set Relationship type to “caused by”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th colspan="5"><strong>Stage 3 — Initial System Architecture Stage</strong></th>
<th></th>
</tr>
<tr>
<th><strong>System Asset to System Action</strong></th>
<th>Asset</th>
<th>Action</th>
<th><strong>performs</strong></th>
<th>This is the functional allocation process at the system-level and ensures that every action is allocated to an asset.</th>
<th><ol type="1">
<li><p>Go to Schema Editor and create a label “to-be” for Asset and Action classes.</p></li>
<li><p>Go to Database view and apply the label “to-be” to Assets and Actions that belong to the To-be Architecture.</p></li>
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field and enter the query:</p></li>
</ol>
<p><strong>order:number class:Asset label:to-be</strong></p>
<ol start="5" type="1">
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter query:</p></li>
</ol>
<p><strong>order:number class:Action label:to-be</strong></p>
<ol start="7" type="1">
<li><p>Set Relationship type to “performs”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Subsystem Req. to System Req.</strong></th>
<th>Requirement (SubReq)</th>
<th>Requirement (SysReq)</th>
<th><strong>traced to</strong></th>
<th>Confirms every subsystem requirement is grounded in a system requirement. This matrix closes the full requirements chain: User Need → Stakeholder Req → System Req → Subsystem Req. Any SubReq row with no column link is an ungrounded subsystem requirement.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “SUBSYS.1” and select the Subsystem Requirements Document.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SYS.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “traced to”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Requirements to Components</strong></th>
<th>Requirement (SysReq or SubReq)</th>
<th>Asset (component)</th>
<th><strong>satisfied by</strong></th>
<th>Generated from the satisfied by relationship chain through trade study artifacts. Confirms every technical requirement is met by a selected component. This is the primary matrix the industry panel will scrutinise to confirm build-vs-buy decisions are traceable.</th>
<th><p>1. Go to Schema Editor</p>
<p>2. Create Label “Selected Component” for Asset Class and “Technical” for Requirement class.</p>
<p>3. Go to Database view</p>
<p>4. Apply “Selected Component” to each component that was selected after the trade study.</p>
<p>5. Open SRD and create separate technical requirement entities for functional requirements with associated Measure entities. Label these requirements “Technical”.</p>
<p>6. Remove relationship between functional requirements and Measure entities and instead create relationship between technical requirements and Measure entities using “specified by”.</p>
<p>7. Follow the steps 1-6 in Section 3.4.</p>
<p>8. Select “Query” in Yaxis field and create query:</p>
<p>order:number class:"Requirement" label:Technical</p>
<p>9. Press “Update”</p>
<p>10.under "Top (X Axis)" enter the query: order:modified class:Asset label:”Selected Component”</p>
<p>11. Set Relationship type to “satisfied by”.</p>
<p>12. Review traces and save Matrix.</p></th>
</tr>
<tr>
<th><strong>Component to Function</strong></th>
<th>Asset (component)</th>
<th>Action (leaf-level)</th>
<th><strong>performs</strong></th>
<th>Confirms every leaf-level action in the granular action diagram is performed by at least one component asset. Unallocated action columns mean the system has functions with no physical implementation — a critical design gap. Multiple asset rows linked to one action identify redundancy or parallel execution.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field and enter the query:</p></li>
</ol>
<p><strong>order:number class:Asset label:Selected Component</strong></p>
<ol start="3" type="1">
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter query:</p></li>
</ol>
<p><strong>order:number class:Action is:leaf</strong></p>
<ol start="5" type="1">
<li><p>Set Relationship type to “performs”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Interface Req. to Conduit</strong></th>
<th>Requirement</th>
<th>Connection</th>
<th><strong>traced to</strong></th>
<th>Confirms every conduit has a corresponding interface requirement created.</th>
<th><p>1. Go to Schema Editor and create a label “Interface” for the Requirement class.</p>
<p>2. Open the SRD and apply the label “Interface” to all the interface requirements.</p>
<p>3. Follow the steps 1-6 in Section 3.4.</p>
<p>4. Create Y-axis Query type:<br />
Order:number class:Requirement label:Interface</p>
<p>5. Create X-axis Query type:</p>
<p>Order:number class:Conduit</p>
<p>6. Set Relationship type to “traced to”</p>
<p>7. Press Update.</p>
<p>8. Review traces and save Matrix.</p></th>
</tr>
<tr>
<th><strong>Verif. Req. to Subsystem Req.</strong></th>
<th>Verif. Requirement (VR.3)</th>
<th>Requirement (SubReq)</th>
<th><strong>verifies</strong></th>
<th>Confirms every subsystem requirement has a verification path. This is the most detailed verification matrix and often reveals missing test planning. Any SubReq column with no VR row must be addressed before the architecture review.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field and type query:</p></li>
</ol>
<p><strong>order:number number:VR.3.* class:Requirement</strong></p>
<ol start="3" type="1">
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SUBSYS.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “verifies”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Risks to Components</strong></th>
<th>Risk</th>
<th>Asset (component)</th>
<th><strong>caused by</strong></th>
<th>Confirms component-level risks are attached to specific components. Risks with no asset link cannot be managed. Particularly important for COTS/GOTS components where supply chain and obsolescence risks must be explicitly tracked.</th>
<th><ol type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field.</p></li>
<li><p>In Query field, type “order:modified- class:Risk”</p></li>
<li><p>Press “Update”.</p></li>
<li><p>under "Top (X Axis)" enter the query: order:modified class:Asset label:”Selected Component”</p></li>
<li><p>Review traces.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### **3.3 Population Thresholds and What They Signal**

The minimum sizes in Section 3.2 are floors, not targets. The table below explains what different population densities indicate to a reviewer and what action should be taken in each case.

| **Population Level** | **What It Looks Like** | **Signal to Reviewer** | **Likely Root Cause** | **Corrective Action** |
|----|----|----|----|----|
| **Below minimum threshold** | Many empty rows or columns; fewer cells than the minimum size guide | Model is incomplete. Matrix is not reviewable. | Missing entities, missing relationships, or wrong relationship verb used to generate the matrix | Add missing entities; fix relationship verbs per Section 2; re-generate matrix before submission |
| **At minimum (1 link per row/col)** | Every row and column has exactly one populated cell; matrix is diagonal or near-diagonal | Requirements are superficially linked. Coverage is thin. | Requirements were written one-to-one with needs rather than being properly decomposed; or relationships were added to pass the check rather than to reflect the model | Review whether each requirement genuinely traces to only one source. If yes, this is acceptable. If relationships were forced, remove them and re-examine decomposition. |
| **Good coverage (2–4 links per row)** | Most rows have 2–4 populated cells; some concentration in high-priority requirements | Model reflects realistic traceability. Healthy. | Requirements were derived through proper decomposition; multiple user needs support key requirements; multiple verification methods applied to complex requirements | No action needed. Highlight high-link-count requirements in the review presentation as risk-informed priorities. |
| **Dense (5+ links per row)** | Many cells populated; almost every combination has a link | Possible over-linking. Review carefully. | Relationships may have been created indiscriminately to appear thorough; or the model genuinely captures a highly interdependent system | Check that every link reflects a real engineering dependency. Remove links that exist only to populate the matrix. Over-linked matrices obscure genuine priorities. |

### **3.4 How to Generate a Matrix in Innoslate**

To create a Traceability Matrix, simply follow these steps:

1.  Navigate to Database View.

2.  Create an Artifact entity.

3.  Assign the 'Matrix' label on the left sidebar.

4.  Give the Matrix a Number (mandatory) and Name (optional).

5.  Click 'Open' and select Traceability Matrix.

6.  Innoslate will navigate to the Traceability Matrix where the 'Missing Matrix' window will appear.

7.  Select your preferred method to access Y-axis entities, 'Query' or Root 'Entity' from the dropdown menu.

8.  On the left sidebar, select the X-axis via Hierarchy, Query or Related.

9.  (optional) If Query or Hierarchy is selected in step 8, users will then want to select the Relationship desired in the dropdown that appears (or type in the field to pull it up).

10. The Traceability Matrix View will then be completed to create relationships among the entities displayed in the matrix. Select 'Save' on the toolbar.

### 

### **3.5 How to Treat Floating Requirements Identified through Traceability Matrix**

During the process of generating Traceability matrices as instructed in Section 3.2, you may come across floating requirements, i.e. requirements that are not linked to a parent. For these requirements, follow the steps below:

1.  Go to Schema Editor and add a label “Orphan” to the Requirement class.

2.  Open any traceability matrix that contains floating requirements and using the wrench icon on the top-right, select Traceability Assist.

3.  Review the links created by the Assist.

4.  If floating requirements still exist, add a label “Orphan” to those requirements.

5.  To review Orphan requirements, go to Database view.

6.  Create a filter to isolate floating requirements using the query “class:Requirement label:Orphan”

7.  If parent is genuinely missing, create an issue and set the relationship Issue “caused by” Requirement.

## **4.** **End-to-End Traceability Chain Reference**

??? note "Sadaf · 2026-05-21"
    this needs to be consistent with the rest of the guidelines in all the documents.
<!-- comment:33 -->


The diagram below shows the complete LML traceability chain your model should reflect by the end of Gate 4. Each arrow represents a relationship. Where Section 2 has identified a correction, the corrected verb is shown.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>EVIDENCE LAYER</strong></p>
<p><strong>══════════════</strong></p>
<p><strong>Raw Artifact (ART.n)</strong></p>
<p><strong>↑ sourced by</strong></p>
<p><strong>Notes Document Statement (EX.n.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>USER NEEDS LAYER</strong></p>
<p><strong>════════════════</strong></p>
<p><strong>User Need Statement (UN.1.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>STAKEHOLDER REQUIREMENT LAYER</strong></p>
<p><strong>══════════════════════════════</strong></p>
<p><strong>Stakeholder Requirement (SR.1.n) ← verifies ── Verification Requirement (VR.1.n)</strong></p>
<p><strong>↑ traced to ↑ verified by</strong></p>
<p><strong>Test Case</strong></p>
<p><strong>SYSTEM REQUIREMENT LAYER</strong></p>
<p><strong>═════════════════════════</strong></p>
<p><strong>System Requirement (SysReq.n) ← verifies ── Verification Requirement (VR.2.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>↓ sourced by → Trade Study (Artifact) ← enabled by ── Decision</strong></p>
<p><strong>↓ enabled by → Decision ↓ resolves</strong></p>
<p><strong>Risk</strong></p>
<p><strong>SUBSYSTEM REQUIREMENT LAYER</strong></p>
<p><strong>════════════════════════════</strong></p>
<p><strong>Subsystem Requirement (SubReq.n) ← verifies ── Verification Requirement (VR.3.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>↓ specified by → Measure (threshold)</strong></p>
<p><strong>↓ sourced by → Trade Study (Artifact)</strong></p>
<p><strong>ACTION / FUNCTIONAL LAYER</strong></p>
<p><strong>═════════════════════════</strong></p>
<p><strong>Action (leaf-level) ── traced to → Subsystem Functional Requirement</strong></p>
<p><strong>↓ decomposes parent Action</strong></p>
<p><strong>↓ performed by Component Asset</strong></p>
<p><strong>COMPONENT / PHYSICAL LAYER</strong></p>
<p><strong>═══════════════════════════</strong></p>
<p><strong>Subsystem Asset</strong></p>
<p><strong>↓ decomposed by</strong></p>
<p><strong>Component Asset (selected via Trade Study)</strong></p>
<p><strong>↓ performs</strong></p>
<p><strong>Action (leaf-level)</strong></p>
<p><strong>INTERFACE LAYER (cross-cutting)</strong></p>
<p><strong>═══════════════════════════════</strong></p>
<p><strong>Interface Requirement ── traced to → Conduit</strong></p>
<p><strong>I/O Entity ── transferred by → Conduit</strong></p>
<p><strong>RISK LAYER (cross-cutting)</strong></p>
<p><strong>═══════════════════════════</strong></p>
<p><strong>Risk ── caused by → Requirement (SR / SysReq / SubReq)</strong></p>
<p><strong>Risk ── caused by → Component Asset</strong></p>
<p><strong>Risk ── related to → Trade Study (Artifact)</strong></p>
<p><strong>Decision ── resolves → Risk</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Before stage 3, the supervisor should be able to pick any leaf-level action in the action diagram and trace upward through this chain to the raw evidence that originated the need for that function. If any step in the chain breaks — an empty cell in a matrix, a missing relationship, or a non-LML verb — the model is incomplete.

Copy of relationships guidelines

**LML Relationship Correction & Traceability Matrix Guidelines**

Spring 2026 \| Habib University

## **1. Purpose and Scope**

This document provides two sets of guidelines to help you review and improve your Innoslate model.

- Section 2 cross-references every LML relationship name explicitly instructed in the ASEPD deliverables document against LML Specification 2.0, identifies errors and non-standard usage, and gives the correct verb to use instead.

- Section 3 defines which traceability matrices to generate, what entity pairs each matrix covers, and the minimum population thresholds required for a model to be considered reviewable.

These guidelines apply to all three gate stages: Requirements (Gate 2), System Concept (Gate 3), and Initial System Architecture (Gate 4).

> **Note:** All relationship names in LML are bidirectional. The table in Section 2 always states the relationship from the perspective of the first entity in the pair (the source). The inverse is implied.

## **2. LML Relationship Review by Deliverable**

The table below lists every entity pair for which the ASEPD deliverables document instructs a specific relationship name. Each entry is evaluated against LML Specification 2.0 and assigned one of three verdicts:

> **Stage 1— Requirements Stage**

| **Deliverable** | **Entity Pair (Source → Target)** | **Verb** | **Explanation / Action Required** |
|----|----|----|----|
| Raw Evidence(Del. 1) | Notes Document → Raw Artifact | **"related to"** | Relationships that exist between two artifacts are: “related to” and “decomposed by”. Out of the two, “related to” is more appropriate. |
| User Needs(Del. 1) | Statement (UN.1.n) → Statement (Notes Document) | **"traced to"** | LML §3.4.0.2.13 defines traced from/traced to between Statements. Direction is correct: a refined UN Statement is traced to its source Statement in the Notes Document. |
| Stakeholder Req.(Del. 3) | Requirement (SR) → Statement (UN) | **"traced to"** | LML §3.4.11.3 and Fig. 3-1 confirm: Requirement traced from Statement is the primary requirements traceability path. No change needed. |
| Stakeholder Req.(Del. 3) | Requirement (SR) → Issue entity | **"causes"** | LML §3.4.0.2.1 defines causes specifically toward a Risk entity. Since the issue is modelled as a Risk entity, causes is correct. If modelled as a Decision, use results in instead. |
| Stakeholder Req.(Del. 3) | Decision → Risk | **"resolves"** | **Replace relationship between trade study and risk with decision and risk.** It is the decision that resolves the risk. Resolves in LML connects any entity to a Risk entity it closes. If Issue is modelled as Risk, this works. However, the more complete pattern is: Decision resolves Risk, and Decision enabled by Trade Study. |
| Stakeholder Req.(Del. 3) | Decision → Trade Study (Artifact) | **"enabled by"** | LML §3.4.0.2.3 defines enables/enabled by toward Decision. The direction here is correct: Decision enabled by Trade Study Artifact. Ensure the relationship is created on the Decision entity pointing to the Artifact, not the reverse. |
| High-level Action Diagrams(Del. 4) | Action → Requirement | **"traced to"** | satisfies does not exist in base LML 2.0 (Table 3-3). |
| Verif. Req.(Del. 5) | Characteristic → Verif. Requirement | **"specifies"** | LML §3.4.4.2 and §3.4.0.2.12 confirm: Characteristic specifies a Requirement or Verification Requirement. Direction and entity types are correct. |
| Verif. Req.(Del. 5) | Verif. Requirement → Decision | **"enables"** | LML §3.4.0.2.3 defines enables/enabled by toward Decision. Direction is correct: Verification Requirement enables Decision. No change needed. |
| Verif. Req.(Del. 5) | Verif. Requirement → Issue/Risk | **"causes"** | LML §3.4.0.2.1 defines causes specifically toward a Risk entity. Since the issue is modelled as a Risk entity, causes is correct. If modelled as a Decision, use results in instead. |
| Verif. Req.(Del. 5) | Verif. Requirement → Test Case | **"verified by"** | LML §3.4.11.4.2 explicitly defines verifies/verified by between Verification Requirement and Test Case. This is correct. Ensure the relationship direction is verified by placed on the Verification Requirement pointing to the Test Case. |

> **Stage 2 — System Concept Stage**

| **Deliverable** | **Entity Pair (Source → Target)** | **Instructed Verb** | **Explanation / Action Required** |
|----|----|----|----|
| System Req.(Del. 3) | System Requirement → Stakeholder Requirement | **“traced to”** | Neither refines nor satisfies exists in base LML 2.0 Table 3-3. The correct verb is traced from: System Requirement traced from Stakeholder Requirement. This is the same traceability verb used for Stakeholder Requirements tracing to User Needs. Using different verbs for the same traceability pattern breaks the chain. |
| System Req.(Del. 3) | System Requirement → Decision | **"enabled by"** | LML §3.4.0.2.3 defines this correctly. The Decision that drove the system requirement enables it. Ensure the relationship is created on the Requirement entity, pointing to the Decision. |
| System Req.(Del. 3) | System Requirement → Trade Study (Artifact) | **"sourced by"** | derived from does not exist in base LML 2.0. The correct relationship between a Requirement and a supporting Artifact is references / referenced by (§3.4.0.2.8): Requirement references Trade Study Artifact. This captures that the artifact informs the requirement without implying derivation, which is not an LML concept. |
| Verif. Req. forSystem Req. | Verif. Requirement → System Requirement | **"verifies"** | LML §3.4.11.4.2 defines verifies/verified by. This is correct and consistent with the Gate 2 approach. Ensure this relationship is created for every system requirement, not just selected ones. |

> **Stage 3 — Initial System Architecture Stage**

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 22%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr>
<th><strong>Deliverable</strong></th>
<th><strong>Entity Pair (Source → Target)</strong></th>
<th><strong>Instructed Verb</strong></th>
<th><strong>Explanation / Action Required</strong></th>
</tr>
<tr>
<th><p>Low-level Action Diagrams</p>
<p>(Del. 1)</p></th>
<th>Asset → Action</th>
<th><strong>"performs"</strong></th>
<th>LML §3.4.1.2.3 defines performed by / performs. Asset performs Action is the canonical functional allocation relationship. Correct.</th>
</tr>
<tr>
<th><p>Low -level Action Diagrams</p>
<p>(Del. 1)</p></th>
<th>Action → Action (decomposition)</th>
<th><strong>"decomposes"</strong></th>
<th>LML §3.4.0.2.2 defines decomposed by / decomposes. Parent Action decomposed by child Action is standard. Correct.</th>
</tr>
<tr>
<th>Physical I/O(Del. 2)</th>
<th>I/O entity → Conduit</th>
<th><strong>"transferred by"</strong></th>
<th>LML §3.4.5.3.2.2 defines transfers / transferred by between Conduit and Input/Output. The direction here (I/O transferred by Conduit) is correct.</th>
</tr>
<tr>
<th>Physical I/O(Del. 2)</th>
<th>Asset → Asset (hierarchy)</th>
<th><strong>"decomposed by"</strong></th>
<th>Standard LML §3.4.0.2.2. Parent Asset decomposed by child Asset establishes subsystem hierarchy. Correct.</th>
</tr>
<tr>
<th>Subsystem Req. (Del. 5)</th>
<th>Subsystem Req → System Req</th>
<th><strong>Direct relationship doesnt exist.</strong></th>
<th>Use SRD to create relationship between subsystem requirements and system requirements.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Trade Study (Artifact) → Subsystem Requirement</th>
<th><strong>"sourced by"</strong></th>
<th>As noted for Del. 7 high-level actions: satisfies is not in base LML 1.4.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Issue/Risk → Trade Study (Artifact)</th>
<th><strong>"caused by"</strong></th>
<th>LML §3.4.10.2 confirms: Risk caused by other entities, and other entities cause Risk. If the Issue is a Risk entity, caused by from the Risk to the Artifact is valid. Correct.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Decision → Trade Study (Artifact)</th>
<th><strong>"enabled by"</strong></th>
<th>Consistent with Stage 1 and Stage 2 usage. LML §3.4.0.2.3. Correct.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Measure → Requirement</th>
<th><strong>"specifies"</strong></th>
<th>In LML §3.4.0.2.12, specified by is placed on the entity being described, pointing to the Characteristic / Measure. The deliverables document instructs placing the relationship on the Measure entity, which reverses the direction. Corrective action: open each Requirement entity, go to Relationships, and create specified by pointing to the Measure — not the other way around.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Risk → Trade Study (Artifact)</th>
<th><strong>"related to"</strong></th>
<th>LML §3.4.0.2.9 defines related to as a generic peer-to-peer link. It is valid here, though references would be more semantically precise (the Risk is informed by the artifact). Either is acceptable.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Risk → Requirement</th>
<th><strong>"traced from"</strong></th>
<th>LML §3.4.0.2.13 allows traced from across entity classes. A Risk entity traced from a Requirement captures that the risk is tied to that requirement's achievement. Correct.</th>
</tr>
<tr>
<th>Trade Studies(Del. 4 &amp; 7)</th>
<th>Decision (mitigation) → Risk</th>
<th><strong>"resolves"</strong></th>
<th>LML §3.4.0.2.10 defines resolves / resolved by: a Decision resolves a Risk. This is the correct pattern for documenting mitigation decisions. Correct.</th>
</tr>
<tr>
<th>Component TradeStudies (Del. 7)</th>
<th>Component Asset → Subsystem Asset</th>
<th><strong>"decomposed by"</strong></th>
<th>Standard asset hierarchy decomposition (§3.4.0.2.2). Subsystem Asset decomposed by Component Asset. Correct.</th>
</tr>
<tr>
<th>Component TradeStudies (Del. 7)</th>
<th>Component Asset → Action</th>
<th><strong>"performs"</strong></th>
<th>LML §3.4.1.2.3. Correct and consistent with granular action diagram allocation. Must be explicitly set — Innoslate does not propagate this from parent assets.</th>
</tr>
<tr>
<th>Component TradeStudies (Del. 7)</th>
<th>Risk → Component Asset</th>
<th><strong>"related to"</strong></th>
<th>See note above for Trade Studies (Del. 4 &amp; 7). Valid generic link. Acceptable.</th>
</tr>
<tr>
<th>Verif. Req. forSubsystem Req.</th>
<th>Verif. Requirement → Subsystem Requirement</th>
<th><strong>"verifies"</strong></th>
<th>Consistent with Gate 2 and Gate 3. LML §3.4.11.4.2. Correct.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **3. Traceability Matrix Guidelines**

### **3.1 Why Traceability Matrices Matter for Review**

A traceability matrix is a two-dimensional table that confirms every entity in one class is connected to at least one entity in another class through a specific LML relationship. Matrices serve three purposes:

- Completeness check: every row and every column must have at least one cell populated. Sparse rows or columns signal missing relationships, not missing content.

- Correctness check: the relationship verb used to generate the matrix must match the LML 2.0 standard — this is why Section 2 matters before you generate matrices.

- Coverage check: the population density of the matrix indicates whether the engineering work is superficial (one link per row) or thorough (multiple supporting links).

### **3.2 Required Matrices by Gate**

The following table defines the matrices that must be generated, and the LML relationship that drives each one..

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 29%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th><strong>Matrix Name</strong></th>
<th><strong>Row Entity (source)</strong></th>
<th><strong>Column Entity (target)</strong></th>
<th><strong>LML Relationship</strong></th>
<th><strong>Review Purpose</strong></th>
<th><strong>How to Create</strong></th>
</tr>
<tr>
<th colspan="5"><strong>Stage 1 — Requirements Stage</strong></th>
<th></th>
</tr>
<tr>
<th><strong>Stakeholder Req. to User Needs</strong></th>
<th>Requirement (SR)</th>
<th>Statement (UN)</th>
<th><strong>traced to</strong></th>
<th>Confirms every stakeholder requirement traces to at least one user need. Orphan requirements (no column link) are ungrounded and likely invented. Multiple SR rows tracing to the same UN column indicate requirements that may need merging.</th>
<th><ol start="9" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field.</p></li>
<li><p>Enter “class:Requirement order:number number:SR.* class:Requirement”.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter “order:number number:UN.* class:Statement”.</p></li>
<li><p>Set Relationship to “traced to”.</p></li>
<li><p>Review traces.</p></li>
<li><p>Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>High Level Actions/Scenarios to High Level Stakeholder Functional Req.</strong></th>
<th>Action</th>
<th>Requirement (SR)</th>
<th><strong>traced to</strong></th>
<th>Confirms every scenario traces to atleast one stakeholder requirement. We're doing it earlier because at this stage of the project you hadn’t yet decomposed into system requirements, and we want you to verify your functional model has coverage before that decomposition.</th>
<th><p>1. Follow the steps 1-6 in Section 3.4.</p>
<p>2. Select Query in Yaxis field and enter query:</p>
<p><strong>order:modified is:top class:Action</strong></p>
<p>3. Press “Update”</p>
<p>4. Under "Top (X Axis)" enter the query:</p>
<p><strong>order:number number:SR.* class:"Requirement" label:"Functional Requirement"</strong></p>
<p>5. Set Relationship to "traced to".</p>
<p>6. Review traces and save Matrix.</p>
<p>This gives the top level actions from all the action diagrams created.</p></th>
</tr>
<tr>
<th><strong>Verif. Req. to Stakeholder Req.</strong></th>
<th>Verif. Requirement (VR.1)</th>
<th>Requirement (SR)</th>
<th><strong>verifies</strong></th>
<th>Confirms every stakeholder requirement has a verification path. Any SR column with no populated cell means that requirement cannot be objectively proven — it must either be made verifiable or removed.</th>
<th><ol start="9" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “VR.1” and select the Stakeholder Verification Requirements Document. Make sure this document has just the Verification Requirements.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter the query:<br />
query:</p></li>
</ol>
<p><strong>order:number number:SR.* class:"Requirement"</strong></p>
<ol start="14" type="1">
<li><p>Set Relationship to “verifies”.</p></li>
<li><p>Review traces.</p></li>
<li><p>Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th colspan="5"><strong>Stage 2 — System Concept Stage</strong></th>
<th></th>
</tr>
<tr>
<th><strong>System Req. to Stakeholder Req.</strong></th>
<th>Requirement (SysReq)</th>
<th>Requirement (SR)</th>
<th><strong>traced to</strong></th>
<th>Confirms every system requirement is grounded in a stakeholder requirement. Any SysReq row with no SR column link is a gold-plated requirement (added without stakeholder basis). Columns with no row link indicate stakeholder requirements not yet decomposed into system requirements.</th>
<th><ol start="9" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “SYS.1” and select the System Requirements Document. Make sure this document has just the System Requirements.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SR.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “traced to”.</p></li>
<li><p>Review traces.</p></li>
<li><p>Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>System Functional Req. to Scenarios</strong></th>
<th>Requirement (SysReq)</th>
<th>Action</th>
<th><strong>traced to</strong></th>
<th>Confirms every system functional requirement is traced to a scenario. In other words, it confirms that every operational scenario can be executed by the architecture.</th>
<th><p>1. Open the top-level action diagram.</p>
<p>2. Open the Hierarchy or Tree diagram to review the traces between functional requirements/actions and scenarios.</p></th>
</tr>
<tr>
<th><strong>Verif. Req. to System Req.</strong></th>
<th>Verif. Requirement (VR.2)</th>
<th>Requirement (SysReq)</th>
<th><strong>verifies</strong></th>
<th>Confirms every system requirement has a verification path. System requirements are solution-dependent and more specific — most should be directly verifiable. Columns with no row link must be addressed before Gate 3 approval.</th>
<th><ol start="8" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “VR.2” and select the System Verification Requirements Document. Make sure this document has just the Verification Requirements.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SYS.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “verifies”.</p></li>
<li><p>Review traces and Save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Risks to Requirements</strong></th>
<th>Risk</th>
<th>Requirement (SR or SysReq)</th>
<th><strong>caused by</strong></th>
<th>Confirms that identified risks are anchored to specific requirements whose achievement they threaten. A Risk entity with no requirement link is floating and cannot be prioritised. A requirement with many Risk links is a signal of high-risk scope that warrants trade study attention.</th>
<th><ol start="8" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field.</p></li>
<li><p>In Query field, type “order:modified- class:Risk”</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “Stakeholder Requirements Document” for Stakeholder Requirements and “System Requirements Document” for System requirements, respectively in Root Entity.</p></li>
<li><p>Set Relationship type to “caused by”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th colspan="5"><strong>Stage 3 — Initial System Architecture Stage</strong></th>
<th></th>
</tr>
<tr>
<th><strong>System Asset to System Action</strong></th>
<th>Asset</th>
<th>Action</th>
<th><strong>performs</strong></th>
<th>This is the functional allocation process at the system-level and ensures that every action is allocated to an asset.</th>
<th><ol start="9" type="1">
<li><p>Go to Schema Editor and create a label “to-be” for Asset and Action classes.</p></li>
<li><p>Go to Database view and apply the label “to-be” to Assets and Actions that belong to the To-be Architecture.</p></li>
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field and enter the query:</p></li>
</ol>
<p><strong>order:number class:Asset label:to-be</strong></p>
<ol start="13" type="1">
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter query:</p></li>
</ol>
<p><strong>order:number class:Action label:to-be</strong></p>
<ol start="15" type="1">
<li><p>Set Relationship type to “performs”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Subsystem Req. to System Req.</strong></th>
<th>Requirement (SubReq)</th>
<th>Requirement (SysReq)</th>
<th><strong>traced to</strong></th>
<th>Confirms every subsystem requirement is grounded in a system requirement. This matrix closes the full requirements chain: User Need → Stakeholder Req → System Req → Subsystem Req. Any SubReq row with no column link is an ungrounded subsystem requirement.</th>
<th><ol start="8" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Entity” in Y-axis field.</p></li>
<li><p>Enter “SUBSYS.1” and select the Subsystem Requirements Document.</p></li>
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SYS.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “traced to”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Requirements to Components</strong></th>
<th>Requirement (SysReq or SubReq)</th>
<th>Asset (component)</th>
<th><strong>satisfied by</strong></th>
<th>Generated from the satisfied by relationship chain through trade study artifacts. Confirms every technical requirement is met by a selected component. This is the primary matrix the industry panel will scrutinise to confirm build-vs-buy decisions are traceable.</th>
<th><p>1. Go to Schema Editor</p>
<p>2. Create Label “Selected Component” for Asset Class and “Technical” for Requirement class.</p>
<p>3. Go to Database view</p>
<p>4. Apply “Selected Component” to each component that was selected after the trade study.</p>
<p>5. Open SRD and create separate technical requirement entities for functional requirements with associated Measure entities. Label these requirements “Technical”.</p>
<p>6. Remove relationship between functional requirements and Measure entities and instead create relationship between technical requirements and Measure entities using “specified by”.</p>
<p>7. Follow the steps 1-6 in Section 3.4.</p>
<p>8. Select “Query” in Yaxis field and create query:</p>
<p>order:number class:"Requirement" label:Technical</p>
<p>9. Press “Update”</p>
<p>10.under "Top (X Axis)" enter the query: order:modified class:Asset label:”Selected Component”</p>
<p>11. Set Relationship type to “satisfied by”.</p>
<p>12. Review traces and save Matrix.</p></th>
</tr>
<tr>
<th><strong>Component to Function</strong></th>
<th>Asset (component)</th>
<th>Action (leaf-level)</th>
<th><strong>performs</strong></th>
<th>Confirms every leaf-level action in the granular action diagram is performed by at least one component asset. Unallocated action columns mean the system has functions with no physical implementation — a critical design gap. Multiple asset rows linked to one action identify redundancy or parallel execution.</th>
<th><ol start="7" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field and enter the query:</p></li>
</ol>
<p><strong>order:number class:Asset label:Selected Component</strong></p>
<ol start="9" type="1">
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Query” in Top(X axis) and enter query:</p></li>
</ol>
<p><strong>order:number class:Action is:leaf</strong></p>
<ol start="11" type="1">
<li><p>Set Relationship type to “performs”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Interface Req. to Conduit</strong></th>
<th>Requirement</th>
<th>Connection</th>
<th><strong>traced to</strong></th>
<th>Confirms every conduit has a corresponding interface requirement created.</th>
<th><p>1. Go to Schema Editor and create a label “Interface” for the Requirement class.</p>
<p>2. Open the SRD and apply the label “Interface” to all the interface requirements.</p>
<p>3. Follow the steps 1-6 in Section 3.4.</p>
<p>4. Create Y-axis Query type:<br />
Order:number class:Requirement label:Interface</p>
<p>5. Create X-axis Query type:</p>
<p>Order:number class:Conduit</p>
<p>6. Set Relationship type to “traced to”</p>
<p>7. Press Update.</p>
<p>8. Review traces and save Matrix.</p></th>
</tr>
<tr>
<th><strong>Verif. Req. to Subsystem Req.</strong></th>
<th>Verif. Requirement (VR.3)</th>
<th>Requirement (SubReq)</th>
<th><strong>verifies</strong></th>
<th>Confirms every subsystem requirement has a verification path. This is the most detailed verification matrix and often reveals missing test planning. Any SubReq column with no VR row must be addressed before the architecture review.</th>
<th><ol start="7" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field and type query:</p></li>
</ol>
<p><strong>order:number number:VR.3.* class:Requirement</strong></p>
<ol start="9" type="1">
<li><p>Press “Update”.</p></li>
<li><p>Apply filter “Hierarchy” in Top(X axis) and Search for “SUBSYS.1” in Root Entity.</p></li>
<li><p>Set Relationship type to “verifies”.</p></li>
<li><p>Review traces and save Matrix.</p></li>
</ol></th>
</tr>
<tr>
<th><strong>Risks to Components</strong></th>
<th>Risk</th>
<th>Asset (component)</th>
<th><strong>caused by</strong></th>
<th>Confirms component-level risks are attached to specific components. Risks with no asset link cannot be managed. Particularly important for COTS/GOTS components where supply chain and obsolescence risks must be explicitly tracked.</th>
<th><ol start="7" type="1">
<li><p>Follow the steps 1-6 in Section 3.4.</p></li>
<li><p>Select “Query” in Y-axis field.</p></li>
<li><p>In Query field, type “order:modified- class:Risk”</p></li>
<li><p>Press “Update”.</p></li>
<li><p>under "Top (X Axis)" enter the query: order:modified class:Asset label:”Selected Component”</p></li>
<li><p>Review traces.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### **3.3 Population Thresholds and What They Signal**

The minimum sizes in Section 3.2 are floors, not targets. The table below explains what different population densities indicate to a reviewer and what action should be taken in each case.

| **Population Level** | **What It Looks Like** | **Signal to Reviewer** | **Likely Root Cause** | **Corrective Action** |
|----|----|----|----|----|
| **Below minimum threshold** | Many empty rows or columns; fewer cells than the minimum size guide | Model is incomplete. Matrix is not reviewable. | Missing entities, missing relationships, or wrong relationship verb used to generate the matrix | Add missing entities; fix relationship verbs per Section 2; re-generate matrix before submission |
| **At minimum (1 link per row/col)** | Every row and column has exactly one populated cell; matrix is diagonal or near-diagonal | Requirements are superficially linked. Coverage is thin. | Requirements were written one-to-one with needs rather than being properly decomposed; or relationships were added to pass the check rather than to reflect the model | Review whether each requirement genuinely traces to only one source. If yes, this is acceptable. If relationships were forced, remove them and re-examine decomposition. |
| **Good coverage (2–4 links per row)** | Most rows have 2–4 populated cells; some concentration in high-priority requirements | Model reflects realistic traceability. Healthy. | Requirements were derived through proper decomposition; multiple user needs support key requirements; multiple verification methods applied to complex requirements | No action needed. Highlight high-link-count requirements in the review presentation as risk-informed priorities. |
| **Dense (5+ links per row)** | Many cells populated; almost every combination has a link | Possible over-linking. Review carefully. | Relationships may have been created indiscriminately to appear thorough; or the model genuinely captures a highly interdependent system | Check that every link reflects a real engineering dependency. Remove links that exist only to populate the matrix. Over-linked matrices obscure genuine priorities. |

### **3.4 How to Generate a Matrix in Innoslate**

To create a Traceability Matrix, simply follow these steps:

11. Navigate to Database View.

12. Create an Artifact entity.

13. Assign the 'Matrix' label on the left sidebar.

14. Give the Matrix a Number (mandatory) and Name (optional).

15. Click 'Open' and select Traceability Matrix.

16. Innoslate will navigate to the Traceability Matrix where the 'Missing Matrix' window will appear.

17. Select your preferred method to access Y-axis entities, 'Query' or Root 'Entity' from the dropdown menu.

18. On the left sidebar, select the X-axis via Hierarchy, Query or Related.

19. (optional) If Query or Hierarchy is selected in step 8, users will then want to select the Relationship desired in the dropdown that appears (or type in the field to pull it up).

20. The Traceability Matrix View will then be completed to create relationships among the entities displayed in the matrix. Select 'Save' on the toolbar.

### 

### **3.5 How to Treat Floating Requirements Identified through Traceability Matrix**

During the process of generating Traceability matrices as instructed in Section 3.2, you may come across floating requirements, i.e. requirements that are not linked to a parent. For these requirements, follow the steps below:

8.  Go to Schema Editor and add a label “Orphan” to the Requirement class.

9.  Open any traceability matrix that contains floating requirements and using the wrench icon on the top-right, select Traceability Assist.

10. Review the links created by the Assist.

11. If floating requirements still exist, add a label “Orphan” to those requirements.

12. To review Orphan requirements, go to Database view.

13. Create a filter to isolate floating requirements using the query “class:Requirement label:Orphan”

14. If parent is genuinely missing, create an issue and set the relationship Issue “caused by” Requirement.

## **4. End-to-End Traceability Chain Reference**

The diagram below shows the complete LML traceability chain your model should reflect by the end of Gate 4. Each arrow represents a relationship. Where Section 2 has identified a correction, the corrected verb is shown.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>EVIDENCE LAYER</strong></p>
<p><strong>══════════════</strong></p>
<p><strong>Raw Artifact (ART.n)</strong></p>
<p><strong>↑ sourced by</strong></p>
<p><strong>Notes Document Statement (EX.n.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>USER NEEDS LAYER</strong></p>
<p><strong>════════════════</strong></p>
<p><strong>User Need Statement (UN.1.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>STAKEHOLDER REQUIREMENT LAYER</strong></p>
<p><strong>══════════════════════════════</strong></p>
<p><strong>Stakeholder Requirement (SR.1.n) ← verifies ── Verification Requirement (VR.1.n)</strong></p>
<p><strong>↑ traced to ↑ verified by</strong></p>
<p><strong>Test Case</strong></p>
<p><strong>SYSTEM REQUIREMENT LAYER</strong></p>
<p><strong>═════════════════════════</strong></p>
<p><strong>System Requirement (SysReq.n) ← verifies ── Verification Requirement (VR.2.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>↓ sourced by → Trade Study (Artifact) ← enabled by ── Decision</strong></p>
<p><strong>↓ enabled by → Decision ↓ resolves</strong></p>
<p><strong>Risk</strong></p>
<p><strong>SUBSYSTEM REQUIREMENT LAYER</strong></p>
<p><strong>════════════════════════════</strong></p>
<p><strong>Subsystem Requirement (SubReq.n) ← verifies ── Verification Requirement (VR.3.n)</strong></p>
<p><strong>↑ traced to</strong></p>
<p><strong>↓ specified by → Measure (threshold)</strong></p>
<p><strong>↓ sourced by → Trade Study (Artifact)</strong></p>
<p><strong>ACTION / FUNCTIONAL LAYER</strong></p>
<p><strong>═════════════════════════</strong></p>
<p><strong>Action (leaf-level) ── traced to → Subsystem Functional Requirement</strong></p>
<p><strong>↓ decomposes parent Action</strong></p>
<p><strong>↓ performed by Component Asset</strong></p>
<p><strong>COMPONENT / PHYSICAL LAYER</strong></p>
<p><strong>═══════════════════════════</strong></p>
<p><strong>Subsystem Asset</strong></p>
<p><strong>↓ decomposed by</strong></p>
<p><strong>Component Asset (selected via Trade Study)</strong></p>
<p><strong>↓ performs</strong></p>
<p><strong>Action (leaf-level)</strong></p>
<p><strong>INTERFACE LAYER (cross-cutting)</strong></p>
<p><strong>═══════════════════════════════</strong></p>
<p><strong>Interface Requirement ── traced to → Conduit</strong></p>
<p><strong>I/O Entity ── transferred by → Conduit</strong></p>
<p><strong>RISK LAYER (cross-cutting)</strong></p>
<p><strong>═══════════════════════════</strong></p>
<p><strong>Risk ── caused by → Requirement (SR / SysReq / SubReq)</strong></p>
<p><strong>Risk ── caused by → Component Asset</strong></p>
<p><strong>Risk ── related to → Trade Study (Artifact)</strong></p>
<p><strong>Decision ── resolves → Risk</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Before stage 3, the supervisor should be able to pick any leaf-level action in the action diagram and trace upward through this chain to the raw evidence that originated the need for that function. If any step in the chain breaks — an empty cell in a matrix, a missing relationship, or a non-LML verb — the model is incomplete.
