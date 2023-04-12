from django.core.management.base import BaseCommand
from app.models import Profile, Question, Tag, Answer, AnswerMark, QuestionMark
from django.contrib.auth.models import User

import random, string

def gen_random_string(length):
    max_length = random.randint(1, length)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(max_length))

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("ratio", type=int)

    def handle(self, *args, **options):
        ratio = options["ratio"]

        profiles = []

        print("Generating profiles ...", end='')

        for _ in range(ratio):
            profiles.append(
                Profile(
                    user = User.objects.create_user(gen_random_string(150)),
                    login = gen_random_string(150),
                    email = gen_random_string(150),
                    nickname = gen_random_string(25),
                    avatar = "img/ava.png",
                    popularity = random.randint(0, 1000000)
                )
            )

        print("done")

        profiles = Profile.objects.bulk_create(profiles)

        tags = []

        print("Generating tags ...", end='')

        for _ in range(ratio):
            tags.append(
                Tag(
                    name = gen_random_string(25),
                    popularity = random.randint(0, 1000000)
                )
            )

        tags = Tag.objects.bulk_create(tags)

        print("done")

        questions = []

        print("Generating questions ...", end='')

        for i in range(ratio * 10):
            questions.append(
                Question.objects.create(
                    profile = Profile.objects.get(id=random.randint(1, ratio)),
                    theme = gen_random_string(150),
                    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris justo risus, pulvinar vel blandit sed, pharetra sit amet urna. Nunc molestie lacus nec lorem sagittis, ut ullamcorper dolor luctus. Donec facilisis turpis eu quam interdum varius. Fusce eu sodales metus. Maecenas ultrices nibh pellentesque nulla luctus, ut cursus turpis suscipit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam gravida feugiat augue et sagittis.",
                    answers = 0,
                    marks = 0,
                )
            )
            
            tag_ids = random.choices(range(ratio), k=random.randint(1, 4))

            for tag_id in tag_ids:
                questions[-1].tags.add(tags[tag_id])

            questions[-1].save()

        print("done")

        answers = []

        print("Generating answers ...", end='')

        for _ in range(ratio * 100):
            q = random.choice(questions)
            answers.append(
                Answer(
                    profile = random.choice(profiles),
                    question = q,
                    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris justo risus, pulvinar vel blandit sed, pharetra sit amet urna. Nunc molestie lacus nec lorem sagittis, ut ullamcorper dolor luctus. Donec facilisis turpis eu quam interdum varius. Fusce eu sodales metus. Maecenas ultrices nibh pellentesque nulla luctus, ut cursus turpis suscipit. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Nam gravida feugiat augue et sagittis.",
                    is_correct = random.randint(0, 1),
                    marks = 0
                )
            )

            q.answers += 1

        print("done")

        answers = Answer.objects.bulk_create(answers)

        qst = []
        ans = []

        print("Generating marks ...", end='')

        for i in range(ratio * 200):
            if i % 2 == 0:
                q = random.choice(questions)
                qst.append(
                    QuestionMark(
                        profile = random.choice(profiles),
                        question = q,
                        is_like = (i % 3 != 0)
                    )
                )

                q.marks += (i % 3 != 0)
            else:
                a = random.choice(answers)
                ans.append(
                    AnswerMark(
                        profile = random.choice(profiles),
                        answer = a,
                        is_like = (i % 3 != 0)
                    )
                )

                a.marks += (i % 3 != 0)

        print("done")

        QuestionMark.objects.bulk_create(qst)
        AnswerMark.objects.bulk_create(ans)

        Question.objects.bulk_update(questions, ['answers', 'marks'])
        Answer.objects.bulk_update(answers, ['marks'])

