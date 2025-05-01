

# 🌟 Cache Whisperer: GenAI-Powered Cache Replacement Policies

![Banner](https://img.shields.io/badge/Project-Cache%20Whisperer-blueviolet?style=for-the-badge)
![Built with Funsearch](https://img.shields.io/badge/Built%20with-Funsearch-success?style=for-the-badge)
![Powered by GenAI](https://img.shields.io/badge/Powered%20By-GenAI-red?style=for-the-badge)
![ChampSim Integration](https://img.shields.io/badge/Integration-ChampSim-blue?style=for-the-badge)

> **_"Where AI breathes intelligence into the heart of computing: the cache."_**

---

## 🚀 Overview

**Cache Whisperer** is an innovative project under the *GenAI for Computer Systems* course under the guidance of Dr. Samira Mirbagher Ajorpaz, where we explore the frontier of **automatically generating and optimizing cache replacement policies** using **Funsearch** — a novel AI-driven method for scientific discovery.

By blending generative AI with systems engineering, this project pushes the limits of cache efficiency — a cornerstone challenge for modern high-performance architectures.

---

## ✨ Project Highlights

- **AI-Driven Optimization:** Generate cutting-edge cache replacement strategies using Funsearch.
- **System-Level Impact:** Enhance cache effectiveness to reduce misses and optimize runtime performance.
- **Seamless Simulation Pipeline:** Evaluate every generated policy through the trusted **ChampSim** simulator.

---

## 🛠️ Setup Instructions

### 1. Clone and Build ChampSim
Clone the official **ChampSim** repository and build it.  
Make sure it is placed **parallel** to the `cache_replacement_funsearch` project directory:

```
your_workspace/
├── cache_replacement_funsearch/
├── champsim/
```

---

### 2. Create the Traces Directory
Inside `cache_replacement_funsearch/`, create a folder named:

```
traces/
```

---

### 3. Add Trace Files
Download and place the **trace files** you want to evaluate inside the newly created `traces/` folder.  
> 💡 *Tip: Sample HPC traces are widely available for academic and research purposes.*

---

### 4. Set the API key
Generate an API key from the GROQ website.

In the cache_replacement_funsearch/funsearch_cache_optimizer.py file:
set GROQ_API_KEY = "#YOUR_API_KEY" 

Next: 
```bash
pip install groq
```

---

### 5. Run the Funsearch Optimizer
Execute the optimizer script from the root directory:

```bash
python cache_replacement_funsearch/funsearch_cache_optimizer.py
```

This will automatically generate, test, and evaluate new cache replacement policies based on the provided traces.

---

### 6. View Generated Policies
All successfully generated and evaluated cache policies will be saved in the:

```
cache_policies/
```

folder, ready for further analysis and benchmarking!

---

## 📂 Project Structure

```
cache_replacement_funsearch/
├── cache_policies/                # ✨ Folder containing AI-optimized policies
├── traces/                        # 📁 Trace files for evaluation
├── funsearch_cache_optimizer.py   # 🧠 Core Funsearch optimizer script
(ChampSim repository)              # 🚀 ChampSim repo (must be parallel to this project)
```

---

## ⚡ Important Notes

- Ensure all **Funsearch** and **ChampSim** dependencies are properly installed beforehand.
- **Valid and compatible trace files** are required for evaluation.
- **Customization Tip:** You can modify `funsearch_cache_optimizer.py` to fine-tune how policies are generated or scored!

---

# 🌟 Welcome to Cache Whisperer  
> *Unleashing the next evolution of cache intelligence, one policy at a time.*

---

