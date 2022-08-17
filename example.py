import DiMo3d as dm
import sys


def test_3d_func():
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    merged_dir = sys.argv[3]

    sx = 128
    sy = 128
    sz = 128

    threads = 1

    # split domain into overlapping cubes
    nx, ny, nz, overlap = dm.split_domain(input_dir, output_dir, sx, sy, sz, overlap=16)

    # prepare dipha files for each individual cube to compute persistence
    dm.write_dipha_persistence_input(output_dir)

    # run dipha to compute persistence
    dm.compute_dipha_persistence(output_dir, threads)

    # convert dipha outputs to usable format
    dm.convert_persistence_diagram(output_dir, threads)

    # write verts
    dm.write_vertex_files(output_dir, threads)

    # run morse
    dm.graph_reconstruction(output_dir, 256, threads)

    # Merge
    dm.merge(output_dir, merged_dir, 256, 256, nx, ny, nz, sx, sy, sz, overlap, 1)

    #VTK
    dm.write_vtp_graph("results/image_stack_128_128_128_merged/0/0/256/dimo_vert.txt", "results/image_stack_128_128_128_merged/0/0/256/dimo_edge.txt", "results/image_stack_128_128_128_merged/0/0/256/dimo.vtp")


if __name__ == '__main__':
    test_3d_func()
