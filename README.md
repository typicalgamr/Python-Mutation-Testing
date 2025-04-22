# 🧬 Comparative Study of Mutation Testing Tools for Python

This repository presents an in-depth **comparative analysis of three prominent Python mutation testing tools**: **Mutatest**, **Cosmic-Ray**, and **MutPy**. The study assesses each tool based on **fault model coverage**, **equivalent mutant detection**, **execution efficiency**, and **mutant diversity**, using a set of benchmark Python programs and detailed metrics for evaluation.

## 🔬 Tools Compared
Mutatest, Cosmic-Ray, MutPy

## 📁 Benchmark Programs

The evaluation was run on the following Python programs to cover a variety of functionalities:

- `utils.py` – String and file operations  
- `math_utils.py` – Mathematical calculations  
- `inventory.py` – Inventory and stock tracking  
- `library.py` – Cataloging and loan operations

## 📊 Evaluation Metrics (GQM Framework)

- **Fault Model Coverage** – Breadth of mutation operators supported
- **Equivalent Mutant Detection** – Ability to detect non-contributing mutants
- **Execution Efficiency** – Runtime performance
- **Mutant Diversity** – Shannon Entropy-based diversity measurement

  ## 📈 Key Findings

- 🏆 **Mutatest** is the best-performing tool with strong results across all metrics.
- ⚖️ **Cosmic-Ray** offers a solid balance for projects prioritizing performance.
- 📘 **MutPy** is best suited for educational or basic use cases due to its ease of use.

> Shannon Entropy (Mutant Diversity):  
> **Mutatest** – 1.58496  
> **Cosmic-Ray** – 1.53066  
> **MutPy** – Lower, limited diversity


| Tool         | Fault Model Coverage | Equivalent Mutant Detection | Execution Efficiency | Mutant Diversity |
|--------------|----------------------|-----------------------------|----------------------|------------------|
| **Mutatest** | 🟢 High (62.26%)     | 🟢 Above 73%                | 🟢 Optimized         | 🟢 Highest (1.58) |
| **Cosmic-Ray** | 🟡 Moderate (54.72%) | 🟡 ~47%                     | 🟡 Balanced          | 🟡 Moderate       |
| **MutPy**     | 🔴 Low (49.06%)      | 🔴 Minimal                  | 🔴 Slow              | 🔴 Low            |

