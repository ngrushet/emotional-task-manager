from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    login = models.CharField(max_length=255)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    labels = models.ManyToManyField('Label')
    priority = models.PositiveIntegerField(default=1, choices=[(i, i) for i in range(1, 11)])
    parent_task = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subtasks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='created_tasks')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text

class Label(models.Model):
    title = models.CharField(max_length=255)

class Slot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    ts_created = models.DateTimeField(auto_now_add=True)
    ts_updated = models.DateTimeField(auto_now=True)
    ts_finished = models.DateTimeField(null=True)

class Emotion(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    rank = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created = models.DateTimeField(auto_now_add=True)

class TaskResult(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField()
    average_emotional_rank = models.DecimalField(max_digits=3, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)