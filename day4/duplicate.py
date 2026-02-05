raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
print(raw_logs)
unique_users=set(raw_logs)
print("ID05 is a unique user:","ID05"in unique_users)
print("length of raw logs: ",len(raw_logs))
print("length of set:",len(unique_users))

print("unique set of IDs",unique_users)