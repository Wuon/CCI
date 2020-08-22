from collections import defaultdict

studentCoursePairs1 = [
    ["58", "Linear Algebra"],
    ["94", "Art History"],
    ["94", "Operating Systems"],
    ["17", "Software Design"],
    ["58", "Mechanics"],
    ["58", "Economics"],
    ["17", "Linear Algebra"],
    ["17", "Political Science"],
    ["94", "Economics"],
    ["25", "Economics"],
    ["58", "Software Design"],
]

studentCoursePairs2 = [
    ["42", "Software Design"],
    ["0", "Advanced Mechanics"],
    ["9", "Art History"],
]

def findCommonCourses(studentCoursePairs):
    studentIds = []
    graph = defaultdict(set)
    result = {}
    for studentCoursePair in studentCoursePairs: 
        studentId, course = studentCoursePair
        if studentId not in studentIds:
            studentIds.append(studentId)
        graph[studentId].add(course)
    for i, studentId in enumerate(studentIds):
        for j in range(i+1, len(studentIds)):
            common = graph[studentId].intersection(graph[studentIds[j]])
            result[(studentId, studentIds[j])] = list(common) if common else []
    return result


print(findCommonCourses(studentCoursePairs1))
print(findCommonCourses(studentCoursePairs2))
