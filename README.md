# retrograde-data

GIS shapefiles for the retrograde geocoding service (part of [route66](https://github.com/redzilla-org/route66)).

**This is a git submodule.** It is referenced by `route66/retrograde/gis-data/` and consumed at build time by the retrograde Lambda Docker image.

## Structure

```
main/           Runtime resources (packaged into Lambda)
  DATA/         California coastline and hills shapefiles
  files/        California freeway network shapefile
  gis_boundaries/  School districts, subdivisions, ZIP codes
test/           Test fixtures (unit/integration tests)
  fix-file/     GeoPoints test shapefile
```

## Usage in route66

The retrograde Makefile copies these files to the Java classpath before building:

```
main/gis_boundaries/ → California_GIS_Boundaries/src/main/resources/gis_boundaries/
main/files/          → California_GIS_Freeways/src/main/resources/files/
main/DATA/           → California_GIS_Ocean/src/main/resources/DATA/
test/fix-file/       → California_GIS_API/src/test/resources/fix-file/
```

## Do not delete

This repo exists to keep ~30 MB of binary GIS data out of the main route66 checkout. Every CI build that touches retrograde resolves this submodule. Deleting it will break retrograde Lambda deployments.
