# Specification: Generalized Robot Model (GRM)

## 1. Objective
Define a flexible, intermediate data structure that represents a robot's kinematics, geometry, and properties beyond the limitations of URDF.

## 2. Core Concepts
The GRM is based on a **Hierarchical Frame Tree**.

### Frame
The fundamental unit of the model. 
- Represents a coordinate system (CS).
- Has a `ParentFrame` and a `LocalTransform` (relative to parent).
- Can be "linked" to a SolidWorks entity (Coordinate System, Plane, Axis, Point, or Component).

### Link (Body)
Attached to a **Frame**.
- Contains inertial properties (mass, center of gravity, inertia tensor).
- Contains a list of `Visual` and `Collision` geometry references.
- Note: Multiple links can be attached to the same frame (e.g., for multi-mesh bodies), or a frame can have zero links (e.g., a "virtual" frame for a coordinate system).

### Joint
Defines the **Kinematic Constraint** between a `ParentFrame` and a `ChildFrame`.
- Joint types: `Fixed`, `Revolute`, `Prismatic`, `Ball`, `Screw`.
- Includes limits (position, velocity, effort).
- Includes dynamics (damping, friction).

### Sensor
Attached to a **Frame**.
- Extensible metadata for ROS-standard sensors (Camera, Ray, IMU).

## 3. JSON Schema (Example)

```json
{
  "robotName": "MyRobot",
  "rootFrame": {
    "id": "base_frame",
    "name": "Base Frame",
    "transform": { "pos": [0,0,0], "rot": [0,0,0,1] },
    "links": [
      {
        "name": "base_link",
        "inertial": { "mass": 1.0, "origin": [0,0,0] },
        "visuals": [{ "type": "mesh", "uri": "package://..." }]
      }
    ],
    "children": [
      {
        "id": "arm_frame",
        "joint": {
          "type": "revolute",
          "axis": [0,0,1],
          "limits": { "lower": -1.57, "upper": 1.57 }
        },
        "links": [...]
      }
    ]
  }
}
```

## 4. SolidWorks Mapping
- **Component2**: Defaults to a `Frame` + a `Link`.
- **Coordinate System Feature**: Maps to a pure `Frame` node.
- **Reference Plane/Axis**: Maps to a pure `Frame` node with simplified geometry.
- **Mates**: Analyzed to determine the `Joint` parameters.
