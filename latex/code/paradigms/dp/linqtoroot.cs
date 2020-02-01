events
  .Select(e => e.Data.eventWeight)
  .FuturePlot("event_weights", "Sample EventWeights",100, 0.0, 1000.0)
  .Save(hdir);
