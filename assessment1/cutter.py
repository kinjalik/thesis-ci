from yaml import safe_load, safe_dump

original = safe_load(open('generated.yaml').read())

original.pop('Culture and Organization')
original['Test and Verification'].pop('Test-Intensity')
original['Test and Verification'].pop('Dynamic depth for infrastructure')
original['Test and Verification'].pop('Static depth for infrastructure')
original['Test and Verification'].pop('Application tests')

original['Build and Deployment'].pop('Patch Management')
original['Implementation'].pop('Application Hardening')
original['Implementation'].pop('Infrastructure Hardening')

safe_dump(original, open('generated2.yaml', 'w+'))