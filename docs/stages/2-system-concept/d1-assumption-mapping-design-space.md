---
title: "Assumption Mapping & Design Space"
stage: "System Concept"
deliverable_id: stage2-d1
status: draft
last_reviewed: 2026-05-23
---

# Assumption Mapping & Design Space

#### **Purpose**

This document captures the **design space before commitment**.  
You are not choosing a solution yet.

### **B. Core System Functions**

List **what the system must do**, not how. (add all core functions)

| **Function ID** | **Function Description** |
|-----------------|--------------------------|
| F1              |                          |
| F2              |                          |
| F3              |                          |

Functions should be solution-agnostic (e.g. “localize the vehicle” not “run LiDAR SLAM”).

### 

### **C. Design Space Exploration (Concept Fragments)**

For each function, list **fundamentally different mechanisms**. You are encouraged to deliberate on radically different design concepts (don’t hold back)

| **Function** | **Mechanism A** | **Mechanism B** | **Mechanism C** |
|--------------|-----------------|-----------------|-----------------|
| F1           |                 |                 |                 |
| F2           |                 |                 |                 |

> Differences must be architectural or physical, not parameter tuning.

**<u>For example:</u>**

| **Function ↓ / Mechanism →** | **Option 1** | **Option 2** | **Option 3** | **Option 4** |
|----|----|----|----|----|
| Localization | LiDAR SLAM | Vision SLAM | Magnetic Tape | Infrastructure Markers |
| Actuation | Differential Drive | Ackermann | Omnidirectional | Rail-Guided |
| Power | Battery | Solar | Wired | Swappable Packs |

### **D. Assumption Mapping**

List assumptions that **must be true** for a design to succeed.

| **Assumption ID** | **Assumption** | **Why It Matters** | **What Breaks if False** |
|----|----|----|----|
| A1 |  |  |  |
| A2 |  |  |  |

Include at least:

- one environmental assumption

- one user/operator assumption

- one performance/scaling assumption

Another thing that you can consider evaluating is how each possible mechanism operates under the stated assumptions:

**<u>For example:</u>**

| **Assumption ↓ / Mechanism →** | **Mechanism A** | **Mechanism B** | **Mechanism C** |
|----|----|----|----|
| Environment is structured | ✓ | x | ✓ |
| Lighting is stable | x | ✓ | ✓ |
| Infrastructure allowed | ✓ | ✓ | x |
| Human intervention possible | x | ✓ | x |

### 

### **E. Known Unknowns**

| **Unknown** | **Why It’s Uncertain** | **Potential Impact** |
|-------------|------------------------|----------------------|
|             |                        |                      |
