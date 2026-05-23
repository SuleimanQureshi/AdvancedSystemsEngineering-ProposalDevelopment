---
title: "Functional Requirements Document (FRD)"
stage: "Stage Synthesis"
deliverable_id: stage3-d3
status: draft
last_reviewed: 2026-05-23
---

# Functional Requirements Document (FRD)

The Functional Requirements Document (FRD) translates your functional architecture — specifically the assets and the actions allocated to them — into clear, structured, and testable requirements. It provides a functional and performance specification for each component asset in your system.

Think of the FRD as answering a precise question:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Core Question</strong></p>
<p>"What must each subsystem do, and how well must it do it?"</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The FRD sits at a specific point in the MBSE process:

- It is derived after subsystem identification and functional allocation are complete.

- It is solution-aware at the subsystem level, but does not yet prescribe detailed design decisions.

- In MBSE terms– actions become functional requirements, and assets define which subsystem performs each function.

## **2. Why This Deliverable Matters**

By grouping requirement statements by the individual subsystems of your system architecture, you enable the programmatic decision of build vs. buy. Because the FRD captures not only **what each asset must do (its capabilities)** but also **how assets connect to one another (their interfaces)**, it is the foundation for competitive procurement.

Without a well-formed FRD:

- Subsystems cannot be independently developed or procured.

- Integration risks remain hidden until late in the project.

- Verification activities have no clear basis for acceptance criteria.

## 

## **3. Understanding What Innoslate Auto-Generates vs. What You Must Provide**

This is a critical distinction that many frequently misunderstand. The "Generate SRD" function in Innoslate does not produce a complete FRD. It produces a **structured template** populated with **data it can derive from your model**. You are responsible to manually enter the rest.

### **3.1 What Innoslate Generates Automatically**

When you run "Generate SRD" from the Asset Diagram, Innoslate can automatically populate sections that are directly traceable to your model's data:

| **FRD Section** | **Auto-populated?** | **Source in Your Model** |
|----|----|----|
| 3.2 System Capability Requirements | Yes — from actions allocated to assets | Action nodes + Allocate relations in your Asset Diagram |
| 3.3 External Interface Requirements | Partially — from I/O flows on boundary | Conduits / I/O between assets and external actors |
| 3.4 Internal Interface Requirements | Partially — from inter-asset conduits | Conduits linking internal assets to each other |
| 3.5 Internal Data Requirements | Partially — from named flows | Data items modelled on conduits |
| 3.1 Required States and Modes | No — must be manually entered | Scenarios in your parent action diagram (use as input) |
| 3.6 Adaptation Requirements | No — must be manually entered | Domain knowledge / stakeholder input |
| 3.7 Safety Requirements | No — must be manually entered | Hazard analysis, safety standards |
| 3.8 Security & Privacy Requirements | No — must be manually entered | Threat model, applicable regulations |
| 3.9 System Environment Requirements | No — must be manually entered | Operational context, environment constraints |
| 3.10 Computer Resource Requirements | No — leave empty at this stage | Architecture/implementation (deferred) |
| 3.11 System Quality Factors | No — must be manually entered | NFRs: reliability, availability, maintainability, etc. |
| 3.12 Design & Construction Constraints | No — must be manually entered | Standards, physical constraints, materials |
| 3.13–18 Personnel, Training, Logistics, etc. | No — must be manually entered | Stakeholder requirements, logistics analysis |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Key Insight</strong></p>
<p>Innoslate auto-populates requirements that are explicitly modelled — primarily functional capabilities (Section 3.2) and interface flows (Sections 3.3–3.5). Non-functional, safety, security, quality, and constraint requirements are engineering judgements that no tool can derive from an action diagram alone. These must be written by you, informed by your system's operational context and applicable standards.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### **3.2 Maximising Auto-population Quality**

The richness of what Innoslate generates is directly proportional to the quality of your action diagram and physical I/O diagram. Before running "Generate SRD", verify the following:

- Your parent action diagram is decomposed to at least one level below each identified subsystem.

- Multiple scenario blocks exist in the parent diagram to capture distinct operational modes.

- Every action node has an asset allocated to it or performing it (no unallocated functions).

- All conduits carry named inputs and outputs.

- Actions use “satisfies” traceability link with parent system requirement or a stakeholder need. It means this Action is what makes the system satisfy that requirement or need.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Common Mistake</strong></p>
<p>Students often run "Generate SRD" on a shallow model with few allocations, then wonder why the document is nearly empty. The tool reflects your model — it cannot invent content that was never modelled. Build a rich model first.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **4. Step-by-Step Instructions**

### **Step 1 — Pre-flight Checks**

- Confirm your model satisfies the prerequisites in Section 3.2 above.

- Review your physical i/o diagram or asset diagram (if you did generate one from Deliverable 2) for completeness.

**Step 2 - Allocate Assets and Conduits**

Ensure all assets are allocated to actions and conduits to input/outputs. There are two ways to do it:

1.  Using Physical I/O Diagram

    1.  Select each **Asset**, then open the **“Relationships”** tab in the sidebar. Review the **Action(s)** assigned to “performs”.

    2.  Select each **Input/Output**, and select **“Repair”** on the top bar.

    3.  Review the **Conduit** and its attributes.

2.  Using Entity View

    1.  Open **Database** View.

    2.  On the left side bar under **“Classes”**, select **“Asset”**.

        1.  Select each Asset and review its “performs” relationship with Actions.

        2.  To add a new relationship, click the arrow next to **“Add”**:

            1.  Choose **“Relate Existing Entities”** to link an existing Action, or

            2.  Create a new Action if needed.

    3.  On the left side bar under **“Classes”**, select **“Conduit”**.

        1.  Select each conduit and open **“Relationships”** tab and review:

            1.  **“connects to”** relationships with Assets

            2.  **“transfers”** relationships with Inputs/Outputs

        2.  Use the **“Add”** option to create or modify these relationships as needed.

### **Step 3 — Create the Asset Diagram**

If already done in Deliverable 2, skip this step.

1.  Click the 'open' menu button in the Physical I/O Diagram and select Asset Diagram. Innoslate will generate a matching Asset Diagram from the assets and conduits already defined.

2.  Review the generated diagram and adjust the layout for readability. Confirm that all subsystems appear as asset nodes and that interfaces (conduits) are visible between them.

**Step 4 — Verify the Asset Hierarchy**

Check that the decomposition hierarchy of your assets correctly reflects your subsystem structure:

- Your top-level system asset should be at the root.

- Each subsystem is a child of the top-level asset.

- Any sub-assets (components within a subsystem) are children of their parent subsystem.

Use the decomposed by / decomposes relationship in Innoslate to establish parent-child links between assets. This hierarchy is what drives the FRD section structure.

### **Step 5 — Generate the FRD**

1.  Open the Asset Diagram (created in Step 2).

2.  Click the wrench icon at the top-right.

3.  Select "Generate SRD".

4.  When prompted for a baseline name, enter exactly: Functional Requirements Document (FRD).

### **Step 6 — Define Scope (Section 1 of FRD)**

Clearly define the system boundary and operational context. Your scope statement should answer:

- What is the system called, and what is its identification number?

- What is the system intended to do at a high level?

- What is explicitly inside the system boundary, and what is outside?

- Who are the primary users and operators?

### **Step 7 — Add Applicable Documents (Section 2)**

List all standards, regulations, and reference documents that apply to your system. Examples include applicable ISO standards, institutional guidelines, and any parent system specifications. Include document number, title, revision, and date.

### **Step 8 — Complete the Requirements (Section 3)**

Work through subsections 3.2 to 3.5 in order, one at a time.

*Refer to the table in Section 3 of these guidelines to identify which parts are already pre-populated by Innoslate and which ones require you to write content manually.*

**For this stage, focus only on the subsections that are pre-populated by Innoslate.** These sections are automatically generated based on your Action Diagram, Physical I/O Diagram, and Asset Diagram, and together they capture the system’s functional requirements.

**You do not need to work on the remaining subsections right now**—they will be completed in later deliverables.

#### **3.2 System Capability Requirements**

These are the core of the FRD. Innoslate will have pre-populated requirements from your allocated actions, grouped by asset (subsystem). Review each auto-generated requirement and ensure it is:

- Stated in "shall" language ("The \[subsystem\] shall...").

- Testable — you must be able to define an objective pass/fail criterion.

- Complete — covering both the function and its performance threshold where applicable.

- Traceable — linked back to the action in the functional model.

***Note:** Add performance attributes (rate, accuracy, latency, capacity) manually. Innoslate generates the functional statement but not the quantitative threshold.*

#### **3.3 External Interface Requirements**

Describe how the system interacts with external entities (users, other systems, the environment). For each external interface specify: what data or energy crosses it, in which direction, at what rate, and in what format.

#### **3.4 Internal Interface Requirements**

Describe interfaces between internal subsystems. Include the interface control data: signal type, protocol, data format, timing, and error handling. Innoslate will partially populate this from inter-asset conduits; review and add detail.

#### **3.5 Internal Data Requirements**

List internal data structures, signals, and storage elements that the system must manage. Specify data types, ranges, retention requirements, and update rates. Do not describe implementation (e.g., no database schema detail).

### **Step 9 — Establish links**

??? note "Sadaf · 2026-05-06"
    write instructions on establishing links between actions/assets and requirements generated by SRD because "Generate SRD" doesnt automatically create these links
<!-- comment:15 -->


### **Step 9 — Verification Requirements (Section 4)**

Section 4 of FRD describes the verification methods for each requirement.

**Since this is part of the verification plan, we leave this out.**

### **Step 10 — Requirements Traceability (Section 5)**

**5. Requirements Traceability**

Section 5 describes the traceability between different levels of the system and the requirements in this document. At the system-level, each requirement must connect to a Stakeholder Need and a subsystem-level requirement. **Fill subsection 5.1 only.**

**5.1 Traceability to Capability Document**

Describe the traceability of subsystem functional requirements populated in this document with the parent system requirements. **Make sure to have created a traceability matrix between the two entities so it can automatically be included**.

### **Step 11 — Review Appendix (Section 6)**

Review sections 6.1-6.3.

del 4 - trade studies
