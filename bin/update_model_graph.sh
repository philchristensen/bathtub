#!/bin/bash

python manage.py graph_models common
dot -Tpng docs/images/common_models.dot > docs/images/common_models.png