# RAG Failure Lab

An engineering lab for diagnosing RAG failures across document processing, retrieval, context assembly, and answer generation.

The project investigates why a RAG system may produce an unreliable answer with confidence: it may miss part of the evidence chain, use an inapplicable document version, smooth over conflicting sources, or answer when the available evidence is insufficient.

## Goal

Build a small, reproducible testbed for investigating specific causes of RAG failures. For each experiment, compare a baseline with a bounded change and inspect not only the final answer but also the trace: which documents and chunks were retrieved, what entered the context, which sources were cited, and what decision the system made.

The goal is not to find a universally best RAG system, but to understand what happens in specific scenarios, where a failure occurs, and what trade-offs a change introduces.

## Areas of investigation

- Iterative retrieval: whether additional searches recover missing evidence, and when they add noise or latency.
- Document versions and source conflicts: whether the system retrieves the applicable source and recognizes unresolved contradictions.
- Insufficient evidence: when the system should answer, ask for clarification, or abstain.

These are independent experimental tracks connected by tracing the path from source documents to the final answer.

## Approach

Experiments use a small, controlled Russian-language corpus. It may combine open documents with verifiable provenance and synthetic fixtures for scenarios that need precise control.

Results are interpreted in the context of the selected corpus, model, and configuration. Synthetic scenarios help isolate failure mechanisms, but do not by themselves establish how frequently those failures occur in real-world systems.

## Status

The project is under development. Its architecture, corpus, and experimental settings will evolve as implementation and initial runs provide evidence.

## Technology

Python is the primary language. Specific libraries and execution paths will be added as the experiments require them.

## Limitations

This project is not intended to be a universal benchmark or a production-ready service. Its findings apply to the scenarios and configuration tested; they do not establish that a particular model or method is best for all RAG systems.