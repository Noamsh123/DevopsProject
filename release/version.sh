#!/bin/bash
echo $(echo ${GIT_BRANCH} | cut -d '/' -f 2)