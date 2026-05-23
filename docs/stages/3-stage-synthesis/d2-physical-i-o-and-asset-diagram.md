---
title: "Physical I/O and Asset Diagram"
stage: "Stage Synthesis"
deliverable_id: stage3-d2
status: draft
last_reviewed: 2026-05-23
---

# Physical I/O and Asset Diagram

The Physical I/O Diagram is a formal diagram in Innoslate that integrates your functional model (action diagrams) and your physical model (subsystems/assets) into a single, connected picture. It shows:

- **Assets** — the physical subsystems and external entities of your design, shown as labelled boxes.

- **Conduits** — the physical or electronic pathways through which information, energy, or material flows between assets, shown as connecting lines.

- **Input/Output (I/O) entities** — the specific items that flow along each conduit, shown as labelled parallelograms on or beside the connecting lines.

Think of it as a wiring diagram for your entire system — but instead of electrical wires, the connections represent every type of flow your system needs to support.

You are also optionally going to generate an Asset diagram using the Physical I/O Diagram.

The Asset Diagram is a simplified, companion view of the same information in the Physical I/O Diagram. Where the Physical I/O Diagram includes I/O entities on the conduit lines, the Asset Diagram shows only:

- **Asset** boxes (your subsystems and external entities)

- **Conduit** lines between them (labelled with the conduit type or name, without the detailed I/O entities shown inline)

## **2. Key Concepts**

These three entity types work together. Understanding the distinction between them is essential before you start drawing.

| **Entity** | **What it is** | **How it appears in Innoslate** |
|----|----|----|
| Asset | A physical component, subsystem, or external entity. Anything that does something or that something flows through. | Box (rectangle). Each subsystem you identified in Stage Synthesis is an Asset. External actors (operator, environment) are also Assets. |
| Conduit | The physical or electronic pathway through which something flows. The conduit itself does not perform actions — it only carries things. | Line connecting two Asset boxes. Examples: a mechanical linkage, a data bus, a pipe, a wireless channel, a cable. |
| Input / Output (I/O) | The specific thing flowing along a conduit: a signal, a command, a material, a force, an energy transfer. This is what the conduit carries. | Parallelogram on or beside the conduit line. This is where you name the interface — e.g., "release command," "energy out," "projectile." |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>The critical distinction: Conduit vs. I/O</strong></p>
<p>A conduit is the channel; an I/O is what travels through it. A single conduit can carry multiple I/O entities. For example, a mechanical linkage (conduit) between the Trigger System and the Locking System might carry both a "release command" (I/O) and a "receptacle secured" confirmation (I/O). Name both separately. In Innoslate, you link each I/O to its conduit using the transferred by / transfers relationship.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## **3. Why This Deliverable Matters**

- **It is simultaneously a functional and physical model**. Functional model and physical model stay in sync from the start, rather than being developed separately and reconciled later — a common source of inconsistency in large projects.

- **It is the foundation for simulation**. Physical I/O Diagram lets you verify that your functional logic actually works before any hardware is built, and derive performance requirements (timing, throughput, latency) from the simulation rather than guessing at them.

- **It drives interface capacity and latency requirements.** Once conduits are defined, you can attach performance attributes to them — bandwidth, latency, force, flow rate. These become the non-functional interface requirements that constrain how each conduit must be designed. Without a conduit entity to attach them to, these requirements tend to get lost or never written down at all.

- **It enables the "bottom-up" recovery of requirements from legacy systems**. If you are working with an existing system that has no original requirements documentation, you can model the physical architecture first in the Physical I/O Diagram — placing what exists as Assets and connecting them with Conduits — and then work backwards to identify the functional requirements each connection implies.

- **It explicitly represents the system boundary.** External entities (the operator, the environment, other systems) appear on the diagram alongside internal subsystems. This makes the boundary of your design responsibility visible and reviewable, reducing scope disputes with stakeholders.

- **The FRD in Innoslate is generated from the Asset Diagram** of the system or subsystem of interest. A well-structured Asset Diagram with clear hierarchical decomposition directly determines the quality and completeness of the auto-generated FRD.

## **4. Step-by-Step Instructions**

#### **4a. Review Physical I/O Diagram**

Before decomposing, review the “To-be Architecture’s” high-level physical i/o diagram from Stage 1. Verify that the top-level system Asset is placed at the centre. This is your system boundary. Every other asset placed on the diagram is either a subsystem of this system or an external entity that interacts with it.

#### **4b. Add All Assets**

- Open Decomposition Diagram for the System and add one Asset box for each subsystem you identified in the Subsystem Identification step.

- While creating Assets for subsystems, name and number them as “SUBSYS.1” and add a description.

- Verify Assets for all external entities in your context (operator, environment, any external systems). Arrange them spatially so that assets that exchange many I/Os are placed near each other — this will reduce crossing lines and make the diagram more readable.

> ***Note:** Do not try to put every detail into a single diagram. If a subsystem is complex, you can decompose it into a child diagram. Keep the top-level Physical I/O Diagram to a readable number of assets — aim for no more than 10 to 12 boxes before you consider decomposing.*

#### **4c. Define Conduits Between Subsystem Assets**

Select an Asset, drag the green connection circle to the second Asset, and the I/O creation dialogue will appear. *Use the same instructions given in Stage 1 for specifying conduits.*

At this point you must decide what kind of conduit this is. Be as specific as you can:

- Mechanical linkage (e.g., a latch-and-pin connection)

- Electrical signal line (e.g., a serial data bus)

- Wireless channel (e.g., RF, optical)

- Fluid or pneumatic pathway

- Gravitational / kinetic energy transfer

The conduit type matters because it constrains the I/O entities it can carry and the performance attributes (latency, bandwidth, force, flow rate) that will eventually become non-functional requirements.

#### **4d. Create and Name I/O Entities**

When the I/O creation dialogue appears (triggered by drawing a conduit), name each I/O entity that flows along that conduit. This is the moment where your action diagram interfaces and your physical model are linked together.

For each I/O entity, specify:

1.  **Name:** Use existing I/O entities created during development of Action diagram (e.g., "release command," "energy out," "projectile").

2.  **Type:** Information event, energy transfer, or material transfer — consistent with your action diagram.

3.  **Direction:** Which asset generates this I/O (source) and which receives it (destination). Set the arrow direction in the conduit accordingly.

4.  **Key attributes (where known):** For information events: data type, timing constraints. For energy transfers: magnitude, units. For material transfers: mass, dimensions. These attributes feed directly into performance budgets in the FRD.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th><p><strong>Each I/O you create here is automatically linked to the actions that generate and receive it</strong></p>
<p>Innoslate uses the Physical I/O Diagram dialogue to establish the generates / receives relationships between Actions and I/O entities, and the transferred by / transfers relationship between I/O entities and Conduits. This means every I/O you define here appears automatically in the functional requirements trace. Do not skip naming the generating and receiving actions in the dialogue — these links are how Innoslate knows which subsystem is responsible for each interface requirement.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### **4e. Decompose Where Needed**

If any asset in the diagram is itself composed of sub-assets (for example, the Trigger System contains a Trigger Detection sub-asset and a Trigger Communication sub-asset), open a child Physical I/O Diagram for that asset and repeat Steps 2 through 6 at the lower level. You can repeat this process for each level of decomposition, stopping when you reach a level where a specific COTS/GOTS product or component can be identified.

> ***Note:** You do not need to decompose all assets to the same depth. Decompose where functional complexity or interface risk is highest. Assets that map directly to mature COTS components may not need further decomposition at all.*

#### **4f. Generate Asset Diagram (Optional)**

The easiest way to create the Asset Diagram is to open it directly from the Physical I/O Diagram in Innoslate. Click the 'open' menu button in the Physical I/O Diagram and select Asset Diagram. Innoslate will generate a matching Asset Diagram from the assets and conduits already defined. Review the generated diagram and adjust the layout for readability.

#### **4g. Verify the Asset Hierarchy (Optional)**

Check that the decomposition hierarchy of your assets correctly reflects your subsystem structure:

1.  Your top-level system asset should be at the root.

2.  Each subsystem is a child of the top-level asset.

3.  Any sub-assets (components within a subsystem) are children of their parent subsystem.

Use the decomposed by / decomposes relationship in Innoslate to establish parent-child links between assets. This hierarchy is what drives the FRD section structure.

#### **4h. Check Attribute Completeness (Optional)**

For each asset, confirm that the following attributes are populated where relevant. These attributes feed into the non-functional requirements sections of the FRD:

- Mass (for hardware assets)

- Power consumption

- Cost estimate (even rough order of magnitude)

- COTS/GOTS label (if the asset is an off-the-shelf component)

- External system label (if the asset is outside your design boundary)

> ***Note:** If adding mass or power attributes to a general Asset class causes them to appear inappropriately on non-hardware entities, create a hardware Asset subclass and add the attributes there. This is a known Innoslate practice.*

## **5. References**

- Jackson, P. L. (2009). Getting Design Right: A Systems Approach. CRC Press. — Primary source for subsystem identification (Ch. 4), ODT development, interface identification, interface matrix, and DSM (Ch. 6).

- Dam, S. H. (Real MBSE: Model-Based Systems Engineering Using LML and Innoslate). — Source for functional analysis and allocation process, COTS/GOTS decomposition stopping criteria, interface diagram preparation, and action-to-asset allocation methodology.

del 3 - FRD
