facts={"fever", "cough"}
rules={
    "flu":["fever","cough"],
    "rest":["flu"]
}
def backward(goal):
    if goal in facts:
        return True
    if goal not in rules:
        return False
    return all(backward(x) for x in rules[goal])
goal="rest"

if backward(goal):
    print("Goal proved")
else:
    print("Goal not proved")