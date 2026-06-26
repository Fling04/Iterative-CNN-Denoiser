# Iterative-CNN-Denoiser
Iterative BP CNN denoiser implementation from Tensorflow to PyTorch 2025
# Modernizing an Iterative BP-CNN Decoder: TensorFlow 1.x to PyTorch

A complete migration of a legacy TensorFlow 1.x implementation of the IEEE BP-CNN channel decoder to a modern PyTorch framework.

Original Paper Reference :<link> https://arxiv.org/abs/1707.05697 </link>

---

## Overview

This project modernizes an academic implementation of the **Iterative Belief Propagation-Convolutional Neural Network (BP-CNN)** architecture originally written using TensorFlow 1.1 and Python 3.4.

The original implementation relied on deprecated TensorFlow APIs that are no longer compatible with current Python environments. This project ports the codebase to PyTorch while preserving the original algorithm and experimental workflow.

The goal was not to redesign the model, but to improve maintainability, readability, and compatibility with modern deep learning frameworks.

---

## Motivation

Many influential machine learning papers published before 2018 rely on software stacks that are difficult or impossible to execute today.

This project demonstrates how legacy research software can be migrated to modern frameworks while maintaining the original experimental behavior.

---

## Original Implementation

* TensorFlow 1.1
* Python 3.4
* Session-based execution
* Deprecated APIs
* Legacy project structure

---

## Modernized Implementation

The project converts the original implementation to PyTorch by:

* Replacing TensorFlow 1.x operations with PyTorch modules
* Modernizing the training and inference pipeline
* Updating model loading and execution
* Simplifying project configuration
* Improving readability and maintainability
* Supporting GPU acceleration through PyTorch

---

## System Pipeline

```text
Encoded Message
       ↓
Correlated Noise Channel
       ↓
Belief Propagation Decoder
       ↓
CNN Noise Estimator
       ↓
Updated Log-Likelihood Ratios
       ↓
Belief Propagation
       ↓
Final Decoded Message
```

The CNN estimates residual channel noise after each Belief Propagation stage, allowing iterative refinement of the decoded signal.

---

## Technologies

* Python
* PyTorch
* NumPy
* LDPC Codes
* Belief Propagation
* Convolutional Neural Networks

---

## Key Engineering Contributions

* Migrated a legacy TensorFlow 1.x codebase to PyTorch.
* Preserved the original BP-CNN decoding workflow.
* Updated training, simulation, and evaluation pipelines.
* Improved compatibility with modern Python environments.
* Refactored portions of the codebase for improved readability and maintainability.

---

## Repository Structure

```text
.
├── src/
├── models/
├── simulations/
├── README.md
└── original_tensorflow_reference/
```

---

## References

Original implementation:

Fei Liang, Cong Shen, and Feng Wu,
**"An Iterative BP-CNN Architecture for Channel Decoding under Correlated Noise"**
IEEE Journal of Selected Topics in Signal Processing.
