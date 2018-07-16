Mat class
1.what's a photo?
- electrical charge: 0~255, 8bits or 256 values.
- digital grayscale image: rectangular matrix of number between 0 and 255.
- 1 pixel 1 color.
- green more than red and blue. demosaicing: interpolating values from neighboring pixels.
- In Numpy: iamge is a n-dimensional NumPy array

2.Mat class
- container, serve as matrix

## as image container
# Assignment operation
Mat B(A);
Mat C = A;
# copy part of an image
Mat B(A, Rect(15, 15, 50, 50));
# or
Mat B = A(Range(2, 4), Range(4, 6));
# clone an image with a mask
B = A.cloneTo(B, mask)
# Find rows or cols or channels of a mat object
M.rows;
M.cols;
M.channels()

## as matrix
# create a 3*3 matrix 
Mat M(3,3CV_8UC3, Scalar(0,255,180));
#print matrix
cout << M << endl;
