# coding: utf-8

from __future__ import unicode_literals

import collections

from .customer import teacher, parent, campus, student


class Toggle(collections.namedtuple('Toggle', ['id_', 'name', 'customer', 'master'])):
    """The predefined toggles of customer of vipkid, e.g teacher - grab class."""

    storage = {}

    def __init__(self, id_, name, customer, master):
        if id_ in self.storage:
            raise ValueError('duplicate toggle id : {}'.format(id_))
        constraint = '{0}{1}'.format(name, customer)
        if constraint in self.constraints:
            raise ValueError('conflict constraint : {}'.format(constraint))

        self.storage[int(id_)] = self

    @property
    def constraints(self):
        return ['{0}{1}'.format(t.name, t.customer.id_) for t in self.storage.values()]

    @property
    def masters(self):
        ms = []
        tg = self

        while tg.master:
            ms.append(tg.master)
            tg = tg.master

        return ms

    @classmethod
    def get(cls, id_):
        return cls.storage.get(int(id_))

    @classmethod
    def get_all_by_customer(cls, customer):
        return [t for t in cls.storage.values() if t.customer is customer]

    @classmethod
    def get_by_customer_and_name(cls, customer, name):
        ts = [t for t in cls.storage.values() if t.name == name and t.customer is customer]
        return ts[0] if ts else None

    @classmethod
    def get_multi_by_customer(cls, customer):
        return [v for k, v in cls.storage.iteritems() if v.customer is customer]


# 教师端开关
teacher_overall = Toggle(
    id_=100,
    name='global',
    customer=teacher,
    master=None
)

teacher_snatch_class = Toggle(
    id_=111,
    name='snatch_class',
    customer=teacher,
    master=teacher_overall
)

teacher_class_reminder = Toggle(
    id_=112,
    name='class_reminder',
    customer=teacher,
    master=teacher_overall
)

teacher_24H_booking_notification = Toggle(
    id_=113,
    name='24H_booking_notification',
    customer=teacher,
    master=teacher_overall
)

# 周二和周五发送的referral变化信息推送提醒；
referral_status_updates = Toggle(
    id_=114,
    name='referral_status_updates',
    customer=teacher,
    master=teacher_overall
)

# 跨周求课提醒
priority_booking = Toggle(
    id_=115,
    name='priority_booking',
    customer=teacher,
    master=teacher_overall
)

# 家长端开关
parent_overall = Toggle(
    id_=200,
    name='global',
    customer=parent,
    master=None
)

#  校园端开关
campus_overall = Toggle(
    id_=300,
    name='global',
    customer=campus,
    master=None
)

#  Student端开关
student_overall = Toggle(
    id_=400,
    name='global',
    customer=student,
    master=None
)

