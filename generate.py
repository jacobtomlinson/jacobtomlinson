import jinja2
import yaml

# Set up templates
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
template = templateEnv.get_template("TEMPLATE.md")

# Load config
with open('config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

# Render remplate
print(template.render(
    **config
))