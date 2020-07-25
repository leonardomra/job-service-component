#!/usr/bin/env python3

import connexion
import os
from job_module import encoder


def main():
    print(os.environ['INIT'])
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Job.ai API'}, pythonic_params=True)
    app.run(port=8080, debug=True)

if __name__ == '__main__':
    main()
