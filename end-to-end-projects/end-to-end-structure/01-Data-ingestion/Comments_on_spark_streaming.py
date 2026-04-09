%md

Since databricks manage the spark session there are configurations available for those.
Being Spark an open-source tool it is possible to configure a spark session in a virtual machine, using the compute resources and the cluster configurations from cloud providers directly reason why spark_streaming is called "Direct To",



**3. Spark Structured Streaming (Direct API)**

**Advantages:**

Flexibility: Provides full control over cluster size, performance tuning, and custom logic (e.g., using foreachBatch for custom sinks).
Source Diversity: Can ingest from a wide range of sources beyond cloud files (Kafka, Kinesis, etc.).

**Disadvantages:**

Management Overhead: Requires manual management of infrastructure, checkpointing, and error handling.
Complexity: Requires more boilerplate code compared to DLT's declarative approach.
Best Cases for Usage: SLA-sensitive streaming workloads that require granular control and specific performance tuning.
Ingesting data from sources not directly supported by DLT's declarative syntax (though DLT can often use readStream internally).
Scenarios needing highly custom data sinks or complex, non-standard processing logic.

**Comments:**

Spark Structured Streaming (append/update/complete)
Summary of Performance: The "Update" output mode is designed to output only the rows that have changed since the last trigger. Its speed depends heavily on how efficiently Spark can compute and identify these changes, as well as the chosen execution mode.
- Micro-batch Mode: Provides robust, exactly-once guarantees with latencies in the order of hundreds of milliseconds per trigger.
- Real-Time Mode: Offers ultra-low latency (~1 ms) for suitable queries, though it has different fault-tolerance guarantees (at-least-once). 

**When to use:**

- Uses Dataframe and Dataset APIs
- Micro-Batch Processing
- Exactly once guarantees
- Built-in Fault tolerance
- Scalable to large scale workloads
- Support various sources and sinks

How this meets your requirements:

Cluster Perception (K8s/Autoscaling): By setting maxBytesPerTrigger, you prevent "stragglers." If a massive pile of JSON files arrives, Spark calculates that it needs more tasks than currently available. The Databricks/K8s manager sees the task queue growing and triggers the addition of new worker pods.
Parallelization: Because the script uses the cloudFiles provider, it automatically handles file splitting. Even if one JSON file is huge, Spark will attempt to split it into chunks (if the compression allows) to process it across multiple K8s nodes.
Source Diversity: This uses the cloudFiles format, which is optimized specifically for S3/Cloud storage, outperforming the standard spark.read.json.