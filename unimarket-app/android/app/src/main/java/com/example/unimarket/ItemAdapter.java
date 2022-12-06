package com.example.unimarket;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class ItemAdapter extends RecyclerView.Adapter<ItemAdapter.ViewHolder> {
    ArrayList<PostResponseData> items = new ArrayList<PostResponseData>();

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup viewGroup, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(viewGroup.getContext());
        View itemView = inflater.inflate(R.layout.item, viewGroup, false);

        return new ViewHolder(itemView);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder viewHolder, int position) { //인덱스에 맞는 객체를 찾는다?
//        PostResponseData item1 = new PostResponseData("ta",10000);
        PostResponseData item = items.get(position);
        viewHolder.setItem(item);
    }
    // 받아온 상품 수
    @Override
    public int getItemCount() {
        return items.size();
    }
    //리스트에 아이템 추가
    public void addItem(PostResponseData item) {
        items.add(item);
    }

    public void setItems(ArrayList<PostResponseData> items) {
        this.items = items;
    }

    public PostResponseData getItem(int position) {
        return items.get(position);
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView titleView;
        TextView priceView;

        public ViewHolder(View itemView) {
            super(itemView);

            titleView = itemView.findViewById(R.id.item_title);
            priceView = itemView.findViewById(R.id.item_price);
        }

        public void setItem(PostResponseData item) {
            titleView.setText(item.getTitle());
            priceView.setText(Integer.toString(item.getPrice()));
        }

    }

}
