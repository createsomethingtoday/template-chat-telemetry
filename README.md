# template-chat-telemetry

Hourly aggregate telemetry snapshot for the Webflow Template Chat worker
(`webflow-template-agent`). A scheduled GitHub Action fetches the worker's
keyed read-only summary endpoint and commits it to `summary.json`; a
scheduled Claude routine reads the raw file (the only fetch path its sandbox
egress allows) and posts the daily digest to Slack.

Aggregate counts and spend only — no user data, prompts, or identifiers.

When the worker reports a finding with severity `outage`, the Action opens one
issue labeled `finder-outage` and closes it when a later snapshot is clear.
