install:
		poerty install 

brain-games:
		poerty run brain-games

build:
		poerty build

publish:
		poerty publish --dry-run

package-install:
		pip install --user dist/*.whl