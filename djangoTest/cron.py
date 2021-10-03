from django_cron import CronJobBase, Schedule

from app.post.models import Post


class DeleteVotes(CronJobBase):
    RUN_AT_TIMES = ['00:00',]

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'djangoTest.cron.DeleteVotes'

    def do(self):
        posts = Post.objects.all()
        for item in posts:
            item.amount_of_upvotes = 0
            item.save()