from django.db import models

# Create your models here.


class ProfessionalDevelopment(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    body = models.TextField(default=None, blank=True)
    date = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='professional/', blank=True, null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


class ProfessionalBackground(models.Model):
    title = models.CharField(max_length=255, default=None, blank=True)
    subtitle = models.CharField(max_length=255, default=None, blank=True)
    picture = models.ImageField(upload_to='professional/', blank=True, null=True)

    def __str__(self):
        return self.title


class BestFeatureCounter(models.Model):

    title = models.CharField(max_length=255, default=None)
    ICON_CHOICES = [
                    ("heart", "heart"),
                    ("bicycle", "bicycle"),
                    ("lightning", "bolt"),
                    ("bug", "bug"),
                    ("bell", "bell"),
                    ("birthday-cake", "birthday-cake"),
                    ("gift", "gift"),
                    ("magic", "magic"),
                    ("accusoft", "accusoft"),
                    ("artstation", "artstation"),
                    ("award", "award"),
                    ("balance-scale", "balance-scale"),
                    ("battery-full", "battery-full"),
                    ("bible", "bible"),
                    ("blogger", "blogger"),
                    ("book", "book"),
                    ("brain", "brain"),
                    ("camera-retro", "camera-retro"),
                    ("calendar-check", "calendar-check"),
                    ("charging-station", "charging-station"),
                    ("check-square", "check-square"),
                    ("code", "code"),
                    ("coffee", "coffee"),
                    ("dice-d20", "dice-d20"),
                    ("dna", "dna"),
                    ("dog", "dog"),
                    ("dove", "dove"),
                    ("dragon", "dragon"),
                    ("envira", "envira"),
                    ("envelope-open-text", "envelope-open-text"),
                    ("eye", "eye"),
                    ("feather-alt", "feather-alt"),
                    ("fighter-jet", "fighter-jet"),
                    ("fire", "fire"),
                    ("firs-aid", "first-aid"),
                    ("fish", "fish"),
                    ("flag", "flag"),
                    ("diamant", "gem"),
                    ("gifts", "gifts"),
                    ("globe", "globe"),
                    ("graduation-cap", "graduation-cap"),
                    ("gravity", "grav"),
                    ("smile face", "grin"),
                    ("smile face 2", "grin-alt"),
                    ("smile face star", "grin-stars"),
                    ("smile face hearts", "grin-hearts"),
                    ("smile face wink", "grin-wink"),
                    ("smile face tears", "grin-tears"),
                    ("grip fire", "gripfire"),
                    ("guitar", "guitar"),
                    ("home", "home"),
                    ("handshake", "handshake"),
                    ("hat-wizard", "hat-wizard"),
                    ("heart music foto", "icons"),
                    ("hotel", "hotel"),
                    ("key", "key"),
                    ("leaf", "leaf"),
                    ("lock", "lock"),
                    ("map", "map"),
                    ("music", "music"),
                    ("pencil-alt", "pencil-alt"),
                    ("atom", "react"),
                    ("pergament", "scroll"),
                    ("diamond 2", "sketch"),
                    ("snowflake", "snowflake"),
                    ("spa", "spa"),
                    ("star", "star"),
                    ("store-alt", "store-alt"),
                    ("pro", "themeco"),
                    ("trophy", "trophy"),
                    ("umbrella", "umbrella"),
                    ("umbrella-beach", "umbrella-beach"),
                    ("user", "user"),
                    ("user-check", "user-check"),
                    ("user-circle", "user-circle"),
                    ("user-clock", "user-clock"),
                    ("user-config", "user-cog"),
                    ("user-edit", "user-edit"),
                    ("user-friends", "user-friends"),
                    ("user-graduate", "user-graduate"),
                    ("user-plus", "user-plus"),
                    ("user-tie", "user-tie"),
                    ("user-tag", "user-tag"),
                    ("users", "users"),
                    ("wrench", "wrench"),
                    ("yin-yang", "yin-yang")
                                                ]

    icon = models.CharField(
        max_length=100,
        choices=ICON_CHOICES,
        default=None,
        blank=True
    )

    size = models.CharField(max_length=100, default="2x", blank=True, null=True)

    COLOR_CHOICES = [("cyan", "cyan"),
                     ("indigo", "indigo"),
                     ("blue", "blue"),
                     ("blue-violet", "blue-violet"),
                     ("red", "red"),
                     ("green", "green"),
                     ("amber", "amber"),
                     ("pink", "pink"),
                     ("black", "black")]

    color = models.CharField(
        max_length=100,
        choices=COLOR_CHOICES,
        default=None,
        blank=True,
        null=True
    )

    data_max = models.CharField(max_length=255, default='100', blank=True)
    data_time_speed = models.CharField(max_length=255, default='2000', blank=True)

    def __str__(self):
        return self.title
