# Overview

## Big Picture
The workload layer takes execution traces as inputs and instantiate a ETFeeder object. ETFeeder helps iterate through and manipulate the traces. The workload layer receives events (e.g. communication finished, computation completed) and schedules the next issuable traces to the available hardware resources. Once the operation is completed, an event is sent to the workload layer to begin issuing next iteration of traces. 
