# One object of interest found during a mission
uint32 id                                  # unique per mission
string label                               # detector class, e.g. "fire_extinguisher"
float32 confidence                         # best detector score seen (0-1)
geometry_msgs/PointStamped position        # averaged position, frame_id = "map"
uint32 sightings                           # how many detections were merged into it
bool confirmed                             # true once sightings >= threshold
builtin_interfaces/Time first_seen
builtin_interfaces/Time last_seen
string snapshot_path                       # best image saved to disk