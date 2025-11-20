from dataclasses import dataclass, field


@dataclass(order=True)
class Student:
    id: int
    name: str
    major: str
    courses: list[str] = field(default_factory=list)

    def enroll(self, course: str) -> None:
        if course not in self.courses:
            self.courses.append(course)

    def total_courses(self) -> int:
        return len(self.courses)
    

def main():
    student1 = Student(1, "Alex", "Computer Science")
    student2 = Student(2, "Katie", "Communications")
    student3 = Student(3, "Tia", "Nursing")

    student1.enroll("CS101")
    student1.enroll("CS102")
    student1.enroll("MATH201")

    student2.enroll("COMM3020")
    student2.enroll("COMM4040")
    student2.enroll("ENG1010")

    student3.enroll("NUTR1020")
    student3.enroll("MICR2060")
    student3.enroll("ZOOL2420")

    print(student1)
    print(student2)
    print(student3)

    print(f"{student1.name} is enrolled in {student1.total_courses()} courses.")
    print(f"{student2.name} is enrolled in {student2.total_courses()} courses.")
    print(f"{student3.name} is enrolled in {student3.total_courses()} courses.")

    print(student1 < student2)  # Compare based on id
    print(student2 > student3)  # Compare based on id   
    print(student1 < student3)  # Compare based on id


if __name__ == "__main__":    
    main()