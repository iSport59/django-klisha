# coding=utf-8
#
# Copyright (c) 2008-2013 by zenzire - http://www.zenzire.com
# Author Marcin Mierzejewski
#

import datetime
from django.db import models
from django.utils.translation import ugettext as _
from .managers import PublishedPictureManager


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __unicode__(self):
        return self.title

    def picture(self):
        try:
            return self.picture_set.order_by('-views_counter')[0].picture
        except:
            return None

    @models.permalink
    def get_absolute_url(self):
        return ('category-detail', (), {'slug': self.slug})


class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)

    class Meta:
        ordering = ['title']
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('tag-detail', (), {'slug': self.slug})


class Picture(models.Model):
    published_at = models.DateTimeField(_("Publication date"), default=datetime.datetime.now)
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(unique=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    picture = models.ImageField(upload_to='pictures')
    views_counter = models.PositiveIntegerField(_("Views counter"), default=1, editable=False)

    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)

    objects = models.Manager()
    published_objects = PublishedPictureManager()

    class Meta:
        ordering = ['-published_at']
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    @property
    def is_published(self):
        if self.published_at < datetime.datetime.now():
            return True
        else:
            return False
    @property
    def year(self):
        return self.published_at.year

    @property
    def month(self):
        return self.published_at.strftime("%m")

    @property
    def day(self):
        return self.published_at.strftime("%d")

    def next(self):
        """ Returns next picrure """
        picturesNext = Picture.objects.order_by("published_at").filter(published_at__gt=self.published_at)

        if len(picturesNext) > 0:
            return picturesNext[0]
        else:
            return None

    def previous(self):
        """ Returns previous picture """
        picturesPrevious = Picture.objects.order_by("-published_at").filter(published_at__lt=self.published_at)
        if len(picturesPrevious) > 0:
            return picturesPrevious[0]
        else:
            return None

    @models.permalink
    def get_absolute_url(self):
        return ('picture-detail', (), {'slug': self.slug})

    def __unicode__(self):
        return self.title
