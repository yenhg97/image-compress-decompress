Môi trường: python

Dữ liệu: Ảnh ở định dạng PNG.

Nén: img_compress.py

    Các input cần nhập:
    
    Dòng 7: image = io.imread('tên ảnh muốn nén.png')
    
    Dòng 22: np.save('codebook_tên ảnh.npy',clusters)  
    
    Dòng 23: io.imsave('compressed_tên ảnh.png',labels);
    
Giải nén: image_decompress.py

    Các input cần nhập:
    
    Dòng 6: centers = np.load('tên codebook.npy')
    
    Dòng 8: c_image = io.imread('tên ảnh đã nén.png')
    
    Dòng 15: io.imsave('tên ảnh sau khi giải nén.png',image);
    
