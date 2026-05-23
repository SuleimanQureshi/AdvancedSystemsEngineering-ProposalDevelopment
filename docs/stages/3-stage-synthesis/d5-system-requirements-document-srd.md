---
title: "System Requirements Document (SRD)"
stage: "Stage Synthesis"
deliverable_id: stage3-d5
status: draft
last_reviewed: 2026-05-23
---

# System Requirements Document (SRD)

By this deliverable, two inputs are ready:

1.  The **FRD** (Deliverable 3) produced subsystem-level 'shall' statements derived from allocated actions, with partial performance thresholds.

2.  The **Trade Study** (Deliverable 4) produced quantitative technical specifications and identified a recommended technology class for each subsystem.

At this stage, the SRD is a **rough-cut baseline** — **not a finished specification**. Its purpose is to support a preliminary budget estimate and low-resolution system design. Numbers should be defensible ballpark figures, not precise specifications. A contractor reading this document should understand the approximate performance range and interface character of each subsystem, not be held to exact thresholds.

TBDs are expected and acceptable at this stage, provided they are managed — each one must state what resolves it and who owns it. The only entries that should not be TBD are those derivable directly from the operating environment or the trade study outputs.

## **2. Why this Deliverable Matters**

The SRD consolidates the outputs of Deliverables 3 and 4 into a single baseline document. It serves three purposes:

1.  Translates the trade study's quantitative thresholds into verifiable performance requirements that a contractor can design to.

2.  Establishes interface constraints so that subsystems developed independently can be integrated without late-stage surprises.

3.  Provides a traceable chain from stakeholder need to derived technical requirement, making the basis for every requirement explicit and reviewable.

The trade study (Deliverable 4) is what enables the SRD to go beyond the FRD. Before it, Sections 3.3–3.12 were largely empty. After it, the technology class selection gives enough information to populate these sections at architecture-phase resolution — ballpark thresholds and functional intent, not detailed implementation specifications.

## 

## **3. Reminder - What Not to Specify Yet** 

Over-specification at the architecture phase is as harmful as under-specification. The textbook is explicit: 'Make sure you do not over specify (or specify a particular solution). If necessary, roll back up a level if it looks like you have decomposed too low. Also, define end-to-end performance factors, not detailed ones for each asset.'

The following should not appear in the subsystem SRD at this stage:

- Specific COTS product names, model numbers, or datasheets cited as requirements. The technology class has been selected; the product has not.

- Algorithm names or software library names as requirements. These are implementation choices, not functional requirements.

- Hardware architecture details: processor type, memory size, operating system. These belong in Section 3.10, which is intentionally empty.

- Wiring diagrams, pin assignments, or circuit-level interface specifications. These are component-level design artefacts.

- Calibration procedures, maintenance procedures, or training curricula. These are the output of the system design phase.

| **Important** | *Populating the SRD does not mean completing it. At this stage, some sections will still carry TBD entries. The discipline required is distinguishing between a genuine TBD (the information cannot yet be determined) and an avoidable blank (the information is knowable but has not been derived). Every TBD must be explicitly flagged with what is needed to resolve it and who is responsible.* |
|----|----|

## 

## 

## 

## 

## 

## 

## **4. Step-by-Step Instructions**

Work through the following steps after completing Deliverables 3 (FRD) and 4 (Trade Study). The starting point is the Innoslate-generated SRD from Deliverable 3 with the trade study outputs in hand.

| **Step 1** | **Pre-flight: Confirm Prerequisites Are Complete** |
|------------|----------------------------------------------------|

Before opening the SRD, verify the following are in place:

- The FRD from Deliverable 3 has been generated from the Asset Diagram and reviewed.

- The Technical Requirements Table from Deliverable 4 is complete, with quantitative threshold values for all non-TBD parameters.

- The recommended technology class has been documented and reviewed with the customer.

- The Physical I/O Diagram has named conduits and I/O entities between all subsystem assets.

- Any open items from the trade study are captured as Decision or Issue entities in Innoslate.

| **Step 2** | **Complete Section 3.2 — Capability Requirements** |
|------------|----------------------------------------------------|

Section 3.2 will already be partially populated by Innoslate’s 'Generate SRD' function. Your task is to complete and validate what was generated.

1.  Review every auto-generated 'shall' statement. Confirm it describes what the subsystem does, not how. Rewrite any statement that specifies a technology or implementation at the functional level.

2.  Check for missing functions — actions your subsystem performs that have no corresponding 'shall' statement. **Add these manually**.

3.  For each statement, append the threshold value to the requirement text using the linked **Measure** entity in Innoslate. If no threshold exists, append "TBD".

4.  For each TBD threshold, if an Issue entity is not created, create an **Issue** entity in Innoslate. Record what information is needed to resolve it and assign an owner. Link it to the requirement using **"caused by.**"

5.  Confirm every requirement links to an action in the functional model. For any unlinked requirement, first check whether the allocation link was simply not created — if so, add it. If no corresponding action exists, either add the missing action to the model or remove the requirement if it has no functional basis.

| **Step 4** | **Populate Sections 3.3 - 3.5 — External, Internal Interface and Data Requirements** |
|----|----|

These sections are driven by the Physical I/O Diagram. Open the diagram and work through each conduit systematically.

#### **4a. External Interfaces (Section 3.3)**

Section 3.3 covers interfaces between the system and entities outside the top-level system boundary — operators, external systems, and the environment. Innoslate will partially populate this from your Physical I/O Diagram.

1.  Review each auto-generated entry. Confirm the entity on the other side of the interface is genuinely outside the system boundary. *Any conduit connecting two internal subsystems does not belong here — move it to 3.4.*

2.  Enrich each entry with the implied channel type from the trade study technology class selection — for example, "Ethernet-class communication" or "mechanical mounting interface." **Specific protocols and connector types are TBD pending product selection**.

3.  Append ballpark data rates or timing constraints where reasonably inferable from the technology class or from capability requirements in 3.2. Otherwise mark TBD.

#### **4b. Internal Interfaces (Section 3.4)**

Section 3.4 covers interfaces between internal subsystems. Innoslate will partially populate this from your Physical I/O Diagram.

1.  Review each auto-generated entry. Confirm it identifies the two subsystems the conduit connects, what flows across it, and the direction of flow.

2.  Enrich each entry with the implied channel type from the trade study technology class selection at technology-class level. *Specific protocols are TBD pending product selection.*

3.  Append a ballpark latency allocation where derivable from the end-to-end latency requirement in 3.2 — split it proportionally across conduits as a first approximation. Treat these as initial estimates, not fixed values.

4.  For any interface where the producing subsystem's output and the consuming subsystem's input cannot be confirmed as compatible at this stage, create an Issue entity in Innoslate, assign an owner, and link it to the relevant interface requirement using **"caused by."**

#### **4c. Internal Data (Section 3.5)**

Internal data requirements specify the data items that flow between internal subsystems. At this stage, we will only review the information already entered by you in FRD:

1.  Review the auto-generated entries for completeness.

2.  Append update rates, where derivable, from Section 3.2.

3.  Data types, nominal ranges, and encoding formats all depend on product-level selection, which hasn't happened yet. Mark these TBD.

## **5. Quality Checklist Before Submission**

|  | **Checklist Item** |
|----|----|
| ☐ | Section 3.1 lists all operational modes with entry/exit conditions and notes which Section 3.2 requirements apply in each mode. |
| ☐ | Every auto-generated Section 3.2 requirement has been reviewed for functional language and supplemented with a quantitative performance threshold from the Trade Study. |
| ☐ | Every requirement in Section 3.2 has an upward traceability link to a stakeholder need or system-level requirement, and a downward link to an action in the functional model. |
| ☐ | Sections 3.3 and 3.4 address every conduit visible in the Physical I/O Diagram. No conduit has been omitted. |
| ☐ | All TBD entries across all sections are captured as Decision or Issue entities in Innoslate with owner and target resolution phase. |
| ☐ | No requirement specifies a particular product, algorithm, hardware platform, or protocol at a level that would preclude compliant alternatives. |
| ☐ | Every empty section states 'No requirements of this type apply to this system' with justification rather than being left blank. |

## 

## **6. References**

- Dam, S. H. Real MBSE: Model-Based Systems Engineering Using LML and Innoslate. — Primary source for the SRD structure, synthesis process, FRD guidance, and TBD management.

- Jackson, P. L. (2009). Getting Design Right: A Systems Approach. CRC Press. — Source for subsystem identification, requirements quality criteria, and interface management.

- ASEPD Student Guidelines: Deliverable 3 — Functional Requirements Document (FRD). — Prerequisite document. Sections 3.2, 3.3, 3.4, and 3.5 of the SRD are built directly from the FRD outputs.

- ASEPD Student Guidelines: Deliverable 4 — Trade Studies and Associated Risks. — Prerequisite document. Performance thresholds in Section 3.2 and technology-class-level interface specifications in Sections 3.3–3.4 derive from the trade study outputs.

del 6 - verification reqs
