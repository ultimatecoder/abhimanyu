#! /usr/bin/env python
# -*- coding: utf-8 -*-

import behave
import utils


@behave.then(u'I should be at home page')
def step_impl(context):
    utils.custom_assert(context.browser.current_url, "http://localhost:5000/")
