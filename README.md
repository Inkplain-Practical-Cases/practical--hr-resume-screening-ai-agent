# HR Resume Screening AI Agent

This is an Inkplain **Forward Deployed Engineering — Starter** teaching repository: a six-branch cumulative Python/FastAPI implementation.

## Learning path

| Step | Git branch | Capability |
|---|---|---|
| 1 | [`step-01-receive-authorized-resume-documents`](https://github.com/Inkplain-Practical-Cases/practical--hr-resume-screening-ai-agent/tree/step-01-receive-authorized-resume-documents) | Receive authorized resume documents |
| 2 | [`step-02-extract-and-normalize-qualifications`](https://github.com/Inkplain-Practical-Cases/practical--hr-resume-screening-ai-agent/tree/step-02-extract-and-normalize-qualifications) | Extract and normalize qualifications |
| 3 | [`step-03-index-and-retrieve-evidence-spans`](https://github.com/Inkplain-Practical-Cases/practical--hr-resume-screening-ai-agent/tree/step-03-index-and-retrieve-evidence-spans) | Index and retrieve evidence spans |
| 4 | [`step-04-create-cited-criteria-comparisons`](https://github.com/Inkplain-Practical-Cases/practical--hr-resume-screening-ai-agent/tree/step-04-create-cited-criteria-comparisons) | Create cited criteria comparisons |
| 5 | [`step-05-add-recruiter-review-and-retention`](https://github.com/Inkplain-Practical-Cases/practical--hr-resume-screening-ai-agent/tree/step-05-add-recruiter-review-and-retention) | Add recruiter review and retention |
| 6 | [`step-06-harden-privacy-and-evidence-tests`](https://github.com/Inkplain-Practical-Cases/practical--hr-resume-screening-ai-agent/tree/step-06-harden-privacy-and-evidence-tests) | Harden privacy and evidence tests |

## Run the final project

1. Use Python 3.12 or newer.
2. Copy `.env.example` to `.env` locally, without committing secrets.
3. Run `python -m pip install -r requirements.txt`.
4. Run `python -m pytest -q`.
5. Run `uvicorn app.main:app --reload` and browse `/docs`.

Each STEP branch has a `STEP-N.crd` and `STEP-N.md`. Main contains `FINAL.crd`; a six-tab Simulator project file is generated in Stage 3 of the practical-case flow.

## Reliability and safety notes

This is an **educational reference implementation**, not a deployed production system. External providers and state stores use deterministic local fixtures where specified. Developers must not assume that the demo's in-memory tenancy, store, credential model, fake MCP transport or order reservations are production-hardened. Live service connections and durable transactional production integration require additional design and acceptance testing.

## Continuous integration

GitHub Actions workflow `.github/workflows/ci.yml` runs a seven-branch matrix covering all six cumulative STEP branches and main. The CI status must be checked; a committed workflow alone does not prove tests passed.

## Simulator and portal

The final CRD documents component relationships. The Stage 3 `hr-resume-screening-ai-agent.inkp` project will contain STEP-1 to STEP-6 tabs. Portal tutorials (Stage 4) link source examples to the specific branch so learners see exactly when each capability is introduced.
