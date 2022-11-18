---
tags:
- generated_from_trainer
model-index:
- name: legalBERT_predict
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# legalBERT_predict

This model is a fine-tuned version of [legalBERT/legalBERT-final-model](https://huggingface.co/legalBERT/legalBERT-final-model) on an unknown dataset.
It achieves the following results on the evaluation set:
- eval_loss: 0.6744
- eval_accuracy: 0.5936
- eval_runtime: 12.4824
- eval_samples_per_second: 278.952
- eval_steps_per_second: 34.929
- step: 0

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Framework versions

- Transformers 4.24.0
- Pytorch 1.10.0a0+0aef44c
- Datasets 2.7.0
- Tokenizers 0.13.2
