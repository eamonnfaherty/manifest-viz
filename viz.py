import yaml

content = open('manifest.yaml').read()
manifest = yaml.safe_load(content)

dependencies = list()

dependencies.append("digraph manifest {")
dependencies.append("node [shape=box];")
dependencies.append('"KMSCMKKeys" [shape=box, style=filled, fillcolor=red]')


for baseline_resource in manifest.get("baseline_resources", []):
    name = baseline_resource.get("name")
    for depends_on in baseline_resource.get("depends_on", []):
        dependencies.append(f"{name} -> {depends_on}")

dependencies.append("}")

print("\n".join(dependencies))