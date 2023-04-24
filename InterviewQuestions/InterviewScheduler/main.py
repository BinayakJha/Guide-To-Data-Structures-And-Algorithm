def merge_overlapping_intervals(intervals):
    if len(intervals) == 0:
        return []
    
    intervals.sort(key=lambda x: x["start"]) # sort by start time
    merged = [intervals[0]] # add first interval to merged list

    for current in intervals:
        previous = merged[-1] # get last interval in merged list
        if current["start"] <= previous["end"]:  # check if current interval overlaps with previous interval
            previous["end"] = max(previous["end"], current["end"]) # update previous interval end time with max of previous and current end time
        else: # no overlap
            merged.append(current) # add current interval to merged list
    return merged

    


intervals = [
  { "start": 9, "end": 10.5 },
  { "start": 9.5, "end": 10 },
  { "start": 10 , "end": 11 },
  { "start": 10.5 , "end": 11.5 },
  { "start": 13, "end": 14 },
  { "start": 13.5, "end": 15 }
]

print(merge_overlapping_intervals(intervals))
