---
title: "Verification Requirements"
stage: "Stage Synthesis"
deliverable_id: stage3-d6
status: draft
last_reviewed: 2026-05-23
---

# Verification Requirements

Verification Requirements define, for each system or subsystem requirement, how compliance will be confirmed and what the measurable acceptance criteria are. They answer two questions:

1.  **What method** will be used — Inspection, Analysis, Simulation, Demonstration, or Test.

2.  **What does "passing" look like** — the specific, objective, measurable condition that must be met for the requirement to be considered satisfied.

They are neither the requirements themselves (Section 3) nor full test procedures, but sit between the two: a contractual commitment to how each requirement will be verified, and the basis from which detailed test plans and procedures are later developed.

Verification requirements are derived using the same methodology as Stage 2 and are integrated directly into the SRD, with Section 4 devoted entirely to verification.

## **2. Why this Deliverable Matters**

Verification requirements matter because:

1.  **They expose bad requirements.** If you cannot write a measurable acceptance criterion for a requirement, the requirement itself is probably vague or incomplete. Writing verification requirements forces that problem to the surface early.

2.  **They prevent late surprises.** Discovering mid-test that a requirement needs equipment you don't have, or a measurement that's impossible on the assembled system, is expensive. Defining verification requirements during design surfaces those constraints while they're still cheap to fix.

3.  **They enforce completeness.** In Innoslate, the "Verifies" relationship means every requirement must have an explicit verification path. Nothing can slip through unnoticed.

4.  **They influence design.** Knowing a thermal requirement will be verified by simulation means the team needs a validated thermal model. Knowing it will be verified by test means thermocouple access points need to be designed in. Verification requirements are a design input, not just a test artifact.

**3. Step-by-step Instructions**

**Step 1 - Open System Design Requirements (SRD) Document**

1.  Navigate to your project in Innoslate

2.  Open SRD.

**Step 2 - Locate the subsystem requirement**

1.  In the document tree, navigate to Section 3 where your subsystem requirements are already entered.

2.  Find the specific subsystem requirement you are writing a verification entry for. Read it carefully before proceeding — your verification criterion must directly address what that requirement states.

**Step 3 - Create a new Verification entity**

1.  In the document tree, navigate to Section 4 – Verification Provisions.

2.  Click “Add Child” to create a new Verification entity under Section 4.

**Step 4 - Assign the Requirement ID**

1.  In the “Number” field, assign a unique ID consistent with your project’s numbering convention.

**Step 5 - Set the Verification Method**

1.  In the entity editor, click on “Metadata” and under “Label”, select an appropriate Verification Method. It describes how the parent requirement will be verified. Refer to Table 1.1 for definitions and guidance on choosing the right method.

2.  If multiple methods apply, create a separate entity for each and briefly justify your choice in the description field.

Table 1.1 Verification Methods

| **Method** | **Definition** | **Typical Use** |
|----|----|----|
| Inspection | Visual/physical examination of the item without operation | Dimensional checks, material markings, workmanship |
| Analysis | Mathematical, computational, or logical reasoning to verify a requirement is met | Weight budget calculations, stress analysis, power budgets |
| Demonstration | Operating the system to show it performs a function; no detailed measurements required | Power-on test, mode transitions, operator walkthroughs |
| Simulation / Modeling | Using a model or simulation to verify behavior or performance | Thermal models, RF link budgets, Monte Carlo runs |
| Test | Operating the system and measuring results against acceptance criteria | Environmental testing, performance benchmarking, load tests |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>⚠️ Choosing between methods</strong></p>
<p>A common mistake is defaulting to “Test” for every requirement. Testing is expensive and sometimes infeasible (e.g., you cannot fully test a one-of-a-kind satellite before launch). Use Analysis or Simulation where testing is impractical, and reserve Test for requirements where measured data against acceptance criteria is the only credible proof.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Step 6 - Write the Verification Criteria**

In the “Description” field, write one or more clear, measurable acceptance criteria sentences.

**A good criterion answers three questions:**

- what is being measured or observed,

- how it is measured (instrument, method, procedure), and

- what the quantitative or qualitative pass/fail threshold is.

Example subsystem requirement: “The power subsystem shall supply a regulated 28 VDC ± 0.5 V output under all load conditions.”

❌ Weak criterion: Verify that the power subsystem meets the voltage requirement.

✅ Strong criterion: Measure the output voltage of the power subsystem at minimum, nominal, and maximum load using a calibrated digital multimeter (accuracy ±0.01 V). The measured

value shall be within the range 27.5 VDC to 28.5 VDC at all three load conditions. A single out-of-range reading constitutes a failure.

**Step 6 - Create the ‘Verifies’ relationship**

1.  With the verification entity open, scroll to the Relationships section.

2.  Click “Add Relationship.” Set the relationship type to “Verifies.” In the target field, search for and select the parent subsystem requirement (e.g., PWR-SUB-01). This links your verification entry back to the requirement in the traceability matrix.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>💡 One requirement may have multiple verification entries</strong></p>
<p>It is acceptable (and often required) to have more than one verification entry per requirement — for example, an Analysis entry to show compliance during design, and a Test entry to confirm compliance on the physical article. Each entry should have its own Innoslate entity and its own “Verifies” link back to the requirement.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

**Step 7 - Confirm in the Verification Matrix**

1.  Navigate to Appendix C / Appendix D (Verification Matrix).

2.  Confirm that your new entry appears and is linked to the correct requirement. If it does not appear, revisit step 6 to ensure the “Verifies” relationship was saved correctly.

del 7 - trade studies for component selection

**Trade Studies and Associated Risks**
