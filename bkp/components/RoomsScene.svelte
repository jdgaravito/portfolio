<script>
	import { extend, T } from '@threlte/core';
	import {
		ContactShadows,
		Float,
		Grid,
		MeshLineMaterial,
		OrbitControls,
		RoundedBoxGeometry,
		interactivity
	} from '@threlte/extras';
	import { spring } from 'svelte/motion';

	interactivity();
	const scale = spring(1);
	export let scene_state = false;
</script>

<T.Group>
	<T.Mesh
	position.y={0}
	position.x={0}
	scale={$scale}
	on:pointerenter={() => scale.set(1.5)}
	on:pointerleave={() => scale.set(1)}
	rotation.reorder="YXZ"
	rotation.y={Math.PI / 4}
	castShadow
>
	<T.BoxGeometry args={[1, 2, 1]} />
	<T.MeshStandardMaterial color="#fefae0" />
</T.Mesh>


</T.Group>

<T.PerspectiveCamera
	makeDefault
	position={[-10, 10, 10]}
	on:create={({ ref }) => {
		ref.lookAt(0, 1, 0);
	}}
	fov={15}
>
	<OrbitControls  enableZoom={true} enableDamping   />
	<!-- <OrbitControls autoRotate enableZoom={true} enableDamping autoRotateSpeed={0.5} target.y={1.5} /> -->
</T.PerspectiveCamera>

<T.DirectionalLight intensity={0.8} position={[0, 10, 10]} castShadow />
<T.AmbientLight intensity={0.2} />

<Grid
	position.y={-0.001}
	cellColor="#ffffff"
	sectionColor="#ffffff"
	sectionThickness={0}
	fadeDistance={25}
	cellSize={2}
/>

<ContactShadows scale={10} blur={2} far={2.5} opacity={0.5} />



<T.AxesHelper />
