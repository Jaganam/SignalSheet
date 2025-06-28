with open("1on1_input.txt", "r") as file:
  lines = [line.strip() for line in file.readlines() if line.strip()]

output = []
current = ""
sumOfDecisions = []

for line in lines:
  if "-" in line:
    current = line
    output.append(f"## {current}\n")
  elif line.lower.startswith("top of mind:"):
    output.append(f"**Top of Mind**  \n{line.split(':',1)[1].strip()}\n")
  elif line.lower.startswith("blockers:"):
    output.append(f"**Blockers**  \n{line.split(':',1)[1].strip()}\n")
  elif line.lower.startswith("open threads:"):
    output.append(f"**Open Threads**  \n{line.split(':',1)[1].strip()}\n")
  elif line.lower.startswith("decision:"):
    output.append(f"**Decisions Needed**  \n{line.split(':',1)[1].strip()}\n")
    sumOfDecisions.append(f"- {current.split('-')[[0].strip()}: {decision}")
  elif line.lower.startswith("watch:"):
    output.append(f"**Watch For**  \n{line.split(':',1)[1].strip()}\n")
  else:
    continue

with open("signal_sheet.md","w") as out:
  out.write("# Signal Sheet - Weekly 1:1 Brief\n\n")
  out.write("\n".join(output))

  if sumOfDecisions:
    out.write("### Open Decisions Summary\n")
    for d in sumOfDecisions:
      out.write(f"{d}\n")
    out.write("\n----\n\n")

out.write("\n".join(output))

print("Signal Sheet generated: signal_sheet.md")
