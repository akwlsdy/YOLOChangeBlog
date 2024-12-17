package com.example.myapplication;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.recyclerview.widget.RecyclerView;
import com.squareup.picasso.Picasso;
import java.util.List;

public class ImagesAdapter extends RecyclerView.Adapter<ImagesAdapter.ViewHolder> {

    private List<ImageItem> imageList;

    public static class ViewHolder extends RecyclerView.ViewHolder {
        // 图像和文本视图
        private final ImageView imageView;
        private final TextView textView;

        public ViewHolder(View view) {
            super(view);
            imageView = view.findViewById(R.id.image);
            textView = view.findViewById(R.id.text);
        }

        public ImageView getImageView() {
            return imageView;
        }

        public TextView getTextView() {
            return textView;
        }
    }

    public ImagesAdapter(List<ImageItem> dataSet) {
        imageList = dataSet;
    }

    @Override
    public ViewHolder onCreateViewHolder(ViewGroup viewGroup, int viewType) {
        // 创建新视图
        View view = LayoutInflater.from(viewGroup.getContext())
                .inflate(R.layout.image_item, viewGroup, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(ViewHolder viewHolder, final int position) {
        // 获取元素
        ImageItem item = imageList.get(position);
        viewHolder.getTextView().setText(item.getTitle());
        Picasso.get().load(item.getImageUrl()).into(viewHolder.getImageView());
    }

    @Override
    public int getItemCount() {
        return imageList.size();
    }
}
