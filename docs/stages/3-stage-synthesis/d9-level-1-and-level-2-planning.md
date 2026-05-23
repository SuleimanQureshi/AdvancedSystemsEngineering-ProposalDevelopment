---
title: "Level 1 and Level 2 Planning"
stage: "Stage Synthesis"
deliverable_id: stage3-d9
status: draft
last_reviewed: 2026-05-23
---

# Level 1 and Level 2 Planning

This deliverable moves your project from architecture into execution planning. You have a rough Bill of Materials (BOM) and a preliminary performance analysis from the previous stage.

Now the task is tol structure how the team will actually build, integrate, and verify the system.

Planning in this context is done at two levels, grounded in the IVPM2 hybrid framework:

- **Level 1** planning establishes the phase-oriented roadmap for the entire project (what gets built and in what order across major milestones), while

- **Level 2** planning breaks those phases into short, time-boxed development cycles — called iterations or sprints — that produce something tangible and reviewable at the end of each cycle.

This dual-level structure is deliberately hybrid: it combines the discipline of a stage-gate model with the adaptability of agile iteration. Neither approach alone is sufficient for engineering projects of this complexity.

The waterfall gives you structure and traceability; iteration gives you feedback and the ability to respond when — not if — your BOM assumptions are wrong.

## **2. Why This Deliverable Matters**

Completing this deliverable correctly achieves four things:

- **Makes the schedule concrete**. For the first time your architecture has a timeline that connects specific components to specific weeks and milestones.

- **Surfaces integration risk early.** Short iterations force the team to think about what needs to be true before each piece can be tested — dependency mapping happens naturally.

- **Establishes a feedback loop with your industry partner.** Each iteration ends with a review. That review is where misalignments between your design and their expectations are caught while correction is still cheap.

- **Locks in shared understanding.** A plan agreed upon by the whole team functions as a contract. It defines who is responsible for what, and when. Vague plans produce scope creep; explicit plans produce accountability.

## **3. Background: Why a Hybrid Approach**

### **3.1 The Limits of Purely Predictive Planning**

Traditional project management — the waterfall model — assumes you can specify everything up front and execute against a fixed plan. This works well in construction and physical engineering where the cost of changing a blueprint mid-build is catastrophic. In those contexts, detailed upfront planning is not optional; it is economically necessary.

Your project does not have this property. You have a BOM and a performance estimate, but you do not yet know exactly how the components will behave together, what integration problems will emerge, or whether your performance assumptions will hold under real operating conditions. Committing to a fully detailed 12-week plan at this stage and then executing against it without feedback loops is a known failure mode. The plan becomes fiction.

### **3.2 The Limits of Purely Agile Planning**

Pure agile approaches, on the other hand, **defer structure** in favour of **responsiveness**. This creates its own problems in engineering contexts. Without a phase-gate structure, it is difficult to ensure that critical design reviews happen before irreversible commitments are made, that traceability between requirements and delivered functionality is maintained, or that your industry partner has a predictable schedule to respond to.

Agile also assumes that the team can surface a minimum viable product early and get real feedback quickly. For some subsystems, this is straightforward. For others — where infrastructure must be assembled before any meaningful demonstration is possible — pure iteration without a governing phase structure leads to wasted cycles.

### **3.3 The Hybrid Solution: IVPM2**

The IVPM2 framework (Iterative and Visual Project Management Method) resolves this tension by operating at multiple planning levels simultaneously. The outer structure is phase-oriented: major milestones define what must be achieved and by when. Within each phase, the team works in short iterations that produce real deliverables, hold review meetings, and feed forward into the next cycle. This is Level 1 and Level 2 planning respectively.

| **Level** | **What it is and what it does** |
|----|----|
| **Level 1 — Phase Plan** | Defines the major phases of the project, their milestones (stage gates), and the macro-deliverables each phase must produce. This is your project roadmap. It is created once and updated when gates require re-planning. |
| **Level 2 — Iteration Plan** | Breaks each phase into time-boxed sprints (typically 1–2 weeks). Each sprint has a specific set of tasks drawn from the phase backlog, a daily stand-up cadence, and ends with a review. This is your execution engine. |

A key insight from the hybrid literature is that these levels must remain connected. Level 2 iterations do not exist independently — each one advances the team toward the Phase 1 milestone. If an iteration consistently fails to move the needle on macro-deliverables, that is a signal that the Level 1 plan needs revisiting, not that more iterations are needed.

### **3.4 When to Use More or Less Iteration**

Not every part of your project benefits equally from iterative development. Apply the following judgment:

| **Situation** | **Recommended approach** |
|----|----|
| **Requirements are well-understood and the task is procedural (e.g., manufacturing a bracket to spec)** | Traditional execution within the phase plan. No need for iteration overhead. |
| **The subsystem involves novel integration or uncertain performance (e.g., sensor fusion, firmware, power regulation under load)** | Short iterations with explicit review gates. Get real data in front of the team quickly. |
| **The customer does not yet know exactly what the interface should look like** | Iterative prototyping with frequent demos. Use the sprint review as the feedback mechanism. |
| **Emergency or single-shot situation with no room for trial and error** | Traditional execution with detailed upfront planning. Iteration assumes you can learn from failure. |

## **4. Step-by-Step Instructions**

A template named “Project Plan.xlxs” is provided to you on LMS.

The template you are filling has three row types that map directly onto the two planning levels:

| **Template Row Type** | **Planning Level** | **What it represents** |
|----|----|----|
| **Component** (dark charcoal bar) | — | A major subsystem or area of work. Rows are auto-summed from children. Do not enter story points manually here. |
| **Macro-deliverable** (coloured by phase) | **Level 1** | A major work item within a component. Can span weeks to months. Defines *what* must be produced and by when. |
| **Mid-level deliverable** (light bar) | **Level 2** | A breakdown of a macro into sprint-sized chunks. Each must fit within **≤ 2 weeks** (max 13 story points on the Fibonacci scale). |

Use the guidelines below to fill the template.

### **Step 1 — Identify Your Components**

### **Review your Asset Diagram from Deliverable 5**. 

### **List the major subsystems of your system**. Each allocated subsystem (e.g., Power, Flight Control, Structural Frame, Software, Ground Station) becomes one Component row. Also include a Systems Engineering & Management component. 

### **Add your Component rows to the template** now, before filling any detail. Give each a sequential ID (1, 2, 3, …). Leave the Story Pts, Start Wk, and End Wk columns blank for Component rows — these are auto-summed from children by the template formula. Do not override them.

### 

### 

### **Step 2 — Establish Your Level 1 Phase Plan**

The Level 1 plan is the stage-gate backbone of your project. It defines the phases your system will pass through from your current state (rough BOM and performance analysis) to final demonstration.

1.  **Review project phases and gates in the template and modify, if needed**.

2.  **Define the macro-deliverables for each component in each phase.**

> For each Component row, ask: *what tangible output must this subsystem produce in each phase to satisfy that phase's gate?* Each answer is a Macro-deliverable row. Fill in these columns:

- **ID**: Use the parent Component's number plus a decimal (e.g., 3.1, 3.2, 3.3).

- **Type**: Macro-deliverable.

- **Name**: Name the output, not the activity. Write what will exist when the work is done — e.g., "Power subsystem verified at ≥ 15 W output" rather than "Test the power subsystem."

- **Phase**: Enter the phase code (P1, P2, etc.) or a range (P1–P2) if the macro spans a gate.

- **Start Wk / End Wk**: Assign the week numbers from the table above that correspond to the phase. If a macro spans only part of a phase, narrow the window appropriately.

- **Dur (wks)**: This auto-calculates as End Wk − Start Wk. Do not enter manually.

- **Story Pts**: Leave blank for Macro rows — the template sums from mid-level children.

- **Status**: Set to Planned for all rows at submission time.

3.  **For each gate, define the gate criteria**.

| **Definition** | *A gate criteria is a set of conditions that must be true before the team proceeds. Gate criteria should be derived directly from your verification requirements.* |
|----|----|

### **Step 3 — Build Your Level 2 Iteration Plan**

1.  **Decompose each macro into mid-level deliverables**.

> For each Macro-deliverable row, insert child rows beneath it. Fill in:

- **ID**: Use the macro's number plus a decimal (e.g., 3.1.1, 3.1.2).

- **Type**: Mid-level.

- **Name**: Describe the specific output — what will be demonstrably true when this item is done. "Motor-ESC bench test" is a mid-level deliverable; "work on the motor" is not.

- **Phase**: Inherit from the parent macro, or narrow if this mid-level sits in a specific part of the phase.

- **Start Wk / End Wk**: Assign within the parent macro's window. Mid-level deliverables should be sequential or partially overlapping — they should not all start simultaneously.

- **Story Pts**: Assign using the Fibonacci scale. 13 is the maximum for any single mid-level row. If an item requires more than 13 points, it is too large — split it. Use this scale:

| **Points** | **Approximate effort** |
|------------|------------------------|
| 1          | A few hours            |
| 2          | ~half a day            |
| 3          | ~1 day                 |
| 5          | 2–3 days               |
| 8          | ~1 week                |
| 13         | ~2 weeks (maximum)     |

- **Dependencies**: If this mid-level deliverable cannot start until another is complete, enter that item's ID here (e.g., 3.1.3, 4.1.1). Mapping dependencies now surfaces integration risk before it becomes a problem.

- **Assignees**: Enter initials or names for the team members responsible.

2.  **Prioritize the backlog.**

> Within each phase, order mid-level deliverables so that the highest-uncertainty items come first. Ask: *which 20% of the mid-level items are responsible for 80% of the technical risk?* Those go to the front of the phase. Items that require another item to finish before they can start must appear after their dependency, not before.

3.  **Identify and flag long-lead-time items.**

> Any mid-level deliverable that depends on procurement, lab booking, or external review should be identified now, before the sprint begins. In the template, flag these in the **Notes** column and set their **Start Wk** early enough to run in parallel with other work. Common examples: ordering components (may take 2–4 weeks), booking EMC test chambers, advisor or partner reviews.

4.  **Include gate review preparation as explicit mid-level rows.**

> Every phase-gate review must appear in the plan as a mid-level deliverable, nested under the Systems Engineering & Management component. Each gate review row should list its gate criteria in the **Notes** column and be placed 1–2 weeks before the end of the phase (to allow time for a dry-run).

#### **Step 4 — Connect Level 1 and Level 2**

After populating both levels, **verify that the plan is internally consistent**:

- The **Start Wk** and **End Wk** of every Macro-deliverable row should encompass all of its mid-level children. If a child falls outside its parent's window, either adjust the parent's dates or move the child.

- The **Story Pts** on every Macro-deliverable and Component row should auto-sum from their children. If a Component row shows a manual number instead of a formula, check that you have extended the =SUM(...) range in the template to include any rows you added.

- No phase should be empty for any component that has work in that phase. If a component contributes to Phase 2 but has no mid-level rows in Phase 2, either the decomposition is incomplete or the component's phase assignment is wrong.

- After each sprint in execution, return to the plan and assess gate readiness: are the completed mid-levels sufficient to satisfy the next gate's criteria? If not, update the Level 1 macro windows or add new mid-level rows and document the change as a Decision entity in Innoslate.

## **6. References**

\[1\] Conforto, E.C. and Amaral, D.C. Agile project management and stage-gate model — A hybrid framework for technology-based companies. Journal of Engineering and Technology Management (2016). — Primary source for the IVPM2 framework, the three-level planning model, and the integration of stage-gate with iterative development.

\[2\] Schwaber, K. Agile Project Management Using Scrum. — Source for sprint planning, daily Scrum, sprint review, and sprint retrospective rules and structure.

\[3\] Tolbert, M. and Parente, S. Hybrid Project Management. — Source for the case for hybrid approaches, the limits of purely predictive and purely agile methods, and the role of the Lean principle in iterative development.

\[4\] Dam, S.H. Real MBSE: Model-Based Systems Engineering Using LML and Innoslate. — Source for the synthesis process and documentation of decisions, artifacts, and risks in Innoslate.

overview document
