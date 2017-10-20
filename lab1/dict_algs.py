def children18(emps):
    for i in range(0, len(emps)):
        for x in range(0, len(emps[i]["children"])):
            if emps[i]["children"][x]["age"] > 18:
                print(emps[i]["children"][x]["name"])
ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasya",
        "age": 12,
    }, {
        "name": "petya",
        "age": 10,
    }],
}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 15,
    }],
}
emps = [ivan, darja]
children18(emps)


